import time
import sys

#initialize variables
startTime=time.time()
seconds=0
minutes=0
waitTime=5
stressTime=6
restTime=3
longRestTime=120
sets=4

#Standard timer code (starting Point)
while True:
    try:
        sys.stdout.write("\r{minutes} Minutes {seconds} Seconds".format(minutes=minutes,seconds=seconds)),
        sys.stdout.flush()
        time.sleep(1)
        seconds=int(time.time()-startTime)-minutes*60
        if seconds>=60:
            minutes+=1
            seconds=0
#KeyboardInterreupt doesn't function haven't figured out why yet
    except KeyboardInterrupt, e:
        break

#Main Program
while True:
    try:
        waitTimer
        print('testcomplete')
#WaitTimer function
def waitTimer():
    while waitTime>0
        sys.stdout.write("\rStart {currentSet} Set in {waitTime} Seconds".format(currentSet=currentSet,waitTime=waitTime)),
        sys.stdout.flush()
        time.sleep(1)
        waitTime=int(waitTime-time.time()+startTime)

#StressTimer function

#RestTimer function
