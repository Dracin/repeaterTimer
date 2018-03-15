import time
import sys

#initialize variables
stressTime=6
restTime=3
longRestTime=120
sets=7

seconds=0
minutes=0
waitTime=5
currentSet=1

##Standard timer code (starting Point)
#while True:
#    try:
#        sys.stdout.write("\r{minutes} Minutes {seconds} Seconds".format(minutes=minutes,seconds=seconds)),
#        sys.stdout.flush()
#        time.sleep(1)
#        seconds=int(time.time()-startTime)-minutes*60
#        if seconds>=60:
#            minutes+=1
#            seconds=0
##KeyboardInterreupt doesn't function haven't figured out why yet
#    except KeyboardInterrupt, e:
#        break
#
#WaitTimer function
def waitTimer(waitTime,currentSet):
    startTime=time.time()
    targetTime=startTime+waitTime
    remainingTime=waitTime
    while remainingTime>0:
        sys.stdout.write("\rStart Set {} in {} Seconds".format(currentSet,int(remainingTime))),
        sys.stdout.flush()
        remainingTime=targetTime-time.time()
        time.sleep(0.5)
    print('')
    print('Start Set {} now'.format(currentSet))

#StressTimer function
def stressTimer(waitTime,currentSet):
    startTime=time.time()
    targetTime=startTime+waitTime
    remainingTime=waitTime
    while remainingTime>0:
        sys.stdout.write("\rHold for {} more seconds, Current Set is {}".format(int(remainingTime),currentSet)),
        sys.stdout.flush()
        remainingTime=targetTime-time.time()
        time.sleep(0.5)
    print('')
    print('Short Rest')

#RestTimer function
def restTimer(waitTime,currentSet):
    startTime=time.time()
    targetTime=startTime+waitTime
    remainingTime=waitTime
    while remainingTime>0:
        sys.stdout.write("\rSet {} starts in {} more seconds".format(currentSet,int(remainingTime))),
        sys.stdout.flush()
        remainingTime=targetTime-time.time()
        time.sleep(0.5)
    print('')
    print('Start Set {} now'.format(currentSet))

#Main Program
print(time.strftime('%H:%M'))
waitTimer(waitTime,currentSet)
while currentSet<=sets:
    if currentSet>1:
        restTimer(restTime,currentSet)
    stressTimer(stressTime,currentSet)
    currentSet=currentSet+1
print('Repeater Done, Long Rest')
