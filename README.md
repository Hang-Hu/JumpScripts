## Description

You only have to execute one command in local to push and execute your scripts in target machine through a jumpbox. Edits it if you have more than one jumpbox or you don't use a docker as target machine.

## Usage

1. Edit `USER@IP:/home/USER/docker.py` in local.py to meet your need, if you don't use ssh key, provide a password.
2. Edit jumpbox.py to meet your need.
3. Execute `python local.py`.