import os

os.spawnl(os.P_DETACH,'C:\\Users\\jarosas\\Desktop\\kubectl\\kubectl.exe','kubectl', 'port-forward', 'service/demo-service', '8080:80')
