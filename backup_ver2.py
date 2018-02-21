import os
import time


a = input("Enter the address of files to be backed up")
#files to be backed up
source = ['{}'.format(a)]
#dir where they need to be stored
b = input("Enter the target drive")
target = '{}'.format(b)

#if dir doesnt exist, create one
if not os.path.exists(target):
    os.mkdir(target)

#name of subdirectory in the main directory
today = target + os.sep + time.strftime('%Y%b%d')

if not os.path.exists(today):
    os.makedirs(today)
    print('Successfully created folder', today)

#name of zip archive

now = time.strftime('%H_%M_%S')

targ = now + '.rar'


rar_command = 'rar a -r {0} {1}'.format(today+os.sep+targ, ' '.join(source))

#run the COMMAND

print("Zip command is:")
print(rar_command)
print('running')

if os.system(rar_command) == 0:
    print('successfully backed up in', today+os.sep+targ)
else:
    print('backup failed')
