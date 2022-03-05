import os
from time import sleep
os.system('python /home/pi/folder_name/auto_mount_post_bootup.py')
sleep(1)
os.system('python /home/pi/folder_name/motion_pir_record_pi_cam.py')