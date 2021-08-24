import os
import sys

portDef = 8080
argsn = len(sys.argv)
if argsn > 1:
	portDef = int(sys.argv[1])

print('*********************** FORWARD PORT ('+str(portDef)+')          *********************************')
os.spawnl(os.P_WAIT,'C:\\kubectl\\kubectl.exe','kubectl', 'port-forward', 'service/demo-service', str(portDef)+':80')
