import os
container_id = "041afa3d2080"
copy_file_into_docker = "".join(["docker", " ", "cp", " ",
                                 "/home/dku/docker.py", " ", container_id, ":/root/docker.py"])
execute = "".join(["docker", " ", "exec", " ", container_id, " ", "python", " ", "/root/docker.py"])
os.system("uname -a")
os.system(copy_file_into_docker)
os.system(execute)
