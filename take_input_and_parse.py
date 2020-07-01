import os
import ast
import sys
import time
import pathlib
import cyclo
import basic
import lines_of_code
import local_parser
import main
import feedback

def viewParsed(code):
    while(1):
        slow_print("\nEnter:\ny to view your parsed program\n0 to return to main menu.\n\nAnswer: ")
        ans = str(input()).lower()
        if ans=="q" or "quit" in ans or "exit" in ans or "done" in ans:
            basic.quit()
            break
        
        if ans == "y" or "ye" in ans:
            try:
                print(local_parser.attempt(code))
                break
            except:
                print("Faulty python program. Cannot parse.\n")
                break
            
        elif (ans == 'n' or "no" in ans or ans == '0' or "return" in ans or "back" in ans or "main" in ans or "menu" in ans):
            break
        else:
            slow_print("\nError. Try again. \n")

    return



"""
A generic yes / no function was created at first however for better HCI, we had to have
separate menus at each step in order to establish certain associations of keys with
functions without disturbing the interface. So this function was dumped.

def what_now():
    ans= input('\nEnter y to try again, n to quit program: ').lower()
    if ans== 'y' or ans =='yes' or ans =='ye' or ans == 'yep':
            print('\n\n')
            main()
    elif (ans == 'n' or ans =='no' or ans == 'not'
          or ans == 'q' or ans == 'quit'
          or ans == 'nop' or ans == 'nope'):
        slow_print('Exiting program.')
        time.sleep(1)
        exit()
    else:
        slow_print('Wrong input. Try again.')
        what_now()
"""



def slow_print(string,delay=0.01):
    """this function takes a string and a delay time in seconds as input. This
    delay is the time taken by each character to be printed. Newline characters
    and spaces are not given any delay so that time is not wasted.
    One of the major reasons to integrate this was to try to make the user
    read whatever we were printing on screen. When everything is just simply
    dumped on screen and the size of text to read is huge, more often than not
    the user will not bother reading anything. We do not want that."""
    i=0
    if len(string)>200:
        while(i<200):
            sys.stdout.write(string[i])
            sys.stdout.flush()
            time.sleep(delay)
            i+=1
        print(string[i:])
    else:
        for c in string:
            if c==' ' or c=='\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                continue
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(delay)

def main():
    while(1):
        slow_print("Enter:\n1 if you want to pass python file.\n2 if you want to write program here.\nq to quit program.\nAnswer: ", 0.008)
        ans = input('')
        if ans=='1' or "pas" in ans or "file" in ans:
            code = basic.get() #takes file input
            slow_print("\n\nYou entered the following program:\n\n", 0.001)
            print(code+"\n")
            
        elif ans =='2' or "typ" in ans or "writ" in ans or "scree" in ans:
            code = basic.wants_to_type() #lets user type python program live
            slow_print("\n\nYou entered the following program:\n\n", 0.001)
            print(code+"\n")
        else:
            if ans=='q' or "quit" in ans or "exit" in ans or "done" in ans or "hat" in ans or "bye" in ans:
                slow_print("\nExiting program in ")
                for i in range(3):
                    slow_print(str(3-i)+'...',0.1)
                    time.sleep(0.5)
                exit()
            else:
                slow_print('\nWrong input. \n')
                time.sleep(0.5)
                continue

        try:
            if len(code)<3:
                print("\nFaulty program. Try again.\n")
                continue
            ast.parse(code)
            break
        except:
            print("\nFaulty program. Try again.\n")        
    
    return code

if __name__ == '__main__':
    main()
