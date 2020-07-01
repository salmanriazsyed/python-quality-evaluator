'''

DO NOT ATTEMPT TO RUN THIS PROGRAM WITHOUT INSTALLING THESE FIRST:
Python 3 or above. ( version created in: 3.8 )
Pip

(Make sure you have the following libaries (these come with the basic
version of python, however this software needs them to function:
'os','subprocess'

For installation of pip:
Windows users: https://phoenixnap.com/kb/install-pip-windows
Linux users: https://www.tecmint.com/install-pip-in-linux/

Once you have installed python and pip properly, run this program from shell or any interpreter. If your pip is upgraded
to the latest version already, it might print a red line that reads:
'
ERROR: Could not find a version that satisfies the requirement upgrade (from versions: none)
ERROR: No matching distribution found for upgrade'
'
Do not worry about this.


NOTE: This program uses shell to perform installation of libraries using pip.
Changes made in 'libraries' list and command variable will result in changes in the commands run in shell.
That is why these are hard coded in this program. If you do not know what you are doing, do not make changes
to these variables as this can result in shell injection.
-Salman Riaz & Faizan Azhar

'''


import subprocess

def main():
    libraries = ['ast','pathlib','time','sys'] #add as more external libraries are used. 
    failed =[] #failed installation names will be appended to this list
    flag=0 #to check if all libaries installed successfully
    for i in libraries:
        '''
        different operating systems have different commands for installing libraries
        so we use try and except for error handling
        '''
        try:
            subprocess.Popen("py -m pip install upgrade") #getting latest version of pip
            command = "py -m pip install " + i #this works for windows 10 latest versions
            subprocess.Popen(command)
        except:
            try:
                subprocess.Popen("pip install upgrade")
                command = "pip install " + i #this works for both linux and windows older versions
                subprocess.Popen(command)
            except:
                flag=1 #in case of failure of both
                failed.append(i) #we store the libary names that failed to install
    if flag==0:
        print("All libraries installed successfully.\n\n")
        input("press any key to continue.\n")
        
    else:
        Print("The following libraries failed to install:")
        for i in failed:
            print(i)
            input("press any key to continue.")
        
if __name__ == '__main__':
    main()
