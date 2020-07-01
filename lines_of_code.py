'''This program counts the total number of lines in a code file passed to it as
as a string. As whitespace in python programs is crucial to the program's
functionality, it has to be manipulated with care. However, since the only
function of this program is to count the number of lines in a program it directly
uses the string method 'strip', which removes newline characters, leading and
trailing spaces.

NOTE: Do not edit this function to return the variable 'temp' if you plan on
compiling it afterwards. You can view what the stripped code looks like if you
remove the commented print line above return statement at the end of the try
block of the count function.
'''

import time
import strip_comments
def lines_count(code):
    code = strip_comments.do_string(code)
    try:
        temp=''
        if len(code)>3: #min python program length is 3.
            for i in range(len(code)):
                if i+3 < len(code):
                    if code[i:i+3]=='\n\n': #checking for consecutive newline
                        continue            #characters and ignoring
                    else:
                        temp+=code[i]
                else:
                    break
        else:
            return 0
        temp = temp.rstrip() #using built-in string function to remove whitespaces
        num= temp.count('\n') + 1
        return num

    except:
        print("Error in loc.py : failed to count lines of code. Returning 0.")
        time.sleep(1)
        return 0

    
    '''
    DUMPED CODE:
    
    clean = code.split("\n")
    #print('\n\nCLEAN:\n',clean,sep='')
    clean = str([line for line in clean if line.strip() != ""])
    
    num = 0
    for c in clean:
        if c == '\n':
            num+=1

    return num
    '''

def main():
    import basic
    '''
    importing modules in this way is often discouraged however this makes the
    lines_count function more efficient, optimized and portable.
    '''
    code = basic.main()
    print('Lines of code:',lines_count(code))


if __name__ == '__main__':
    main()

