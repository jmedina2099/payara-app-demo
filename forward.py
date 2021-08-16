import os

os.spawnl(os.P_DETACH,'kubectl port-forward service/demo-service 8080:80')
