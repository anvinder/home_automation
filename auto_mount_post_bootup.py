import os
import subprocess
from time import sleep

subprocess.call("sudo mount -t smb://0.0.0.0/cps".split())
sleep(1)
subprocess.call("sudo mount -t cifs -o username=abc,pass=abc,uid=1000,gid=1000,vers=2.0 //0.0.0.0/cps /home/pi/folder_name/network_drive_to_be_mapped_locally".split())
sleep(1)
