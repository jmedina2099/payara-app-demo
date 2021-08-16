import time
import sys

sleepDef = 230
argsn = len(sys.argv)
if argsn > 1:
	sleepDef = int(sys.argv[1])

print('*********************** WAITING ('+str(sleepDef)+')..             *********************************')
time.sleep(sleepDef)
