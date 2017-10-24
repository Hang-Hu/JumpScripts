import os

os.system("uname -a")
os.system("scp docker.py USER@IP:/home/USER/docker.py")
os.system("ssh docker-host 'python' < docker-host.py")
