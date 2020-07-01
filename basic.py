"""This module is specifically made for the project:

            Software Quality Evaluator for Python
             by Salman Riaz Syed and Faizan Azhar

It allows user to either pass a python file as argument or type a python
program on screen.
"""

import os
import pathlib
import main
import take_input_and_parse

def quit():
    take_input_and_parse.slow_print("\nSafely exiting...\n",0.05)
    exit()

def wants_to_type():
    code=""
    string="""\n\t\tEnter python 3 - 3.8 code. Enter '$' to end program :
\tEnter 0 in the beginning of any line to simply return to main menu.\n\n"""
    take_input_and_parse.slow_print(string)
    while(1):
        line = str(input())
        if len(line)<1:
            continue
        if line[0]=="0":
            main.intro()
        code = code + line #concatenation of string
        if len(line) < 1:
            continue
        if code[-1] == '$':
            code = code[0:-1]
            break
        elif code[-2] == '$':
            code = code[0:-2]
        code = code + '\n'
    file_name='user_code.py'
    file = open(file_name,'w')
    file.write(code)
    return code

def get():
    while(1):
        take_input_and_parse.slow_print("\nEnter file name.\nEntering 0 will take you back to main menu.\n\nAnswer: ")
        file_name = input()
        if file_name=='0':
            main.intro()
            break
        if file_name[-3:] == '.py':
            if os.path.isfile(file_name):
                #print('success')
                break
        else:
            file_name = file_name + '.py'
            #print('file_name + py = ',file_name)
            if os.path.isfile(file_name):
                    #print('success')
                    break

        #this serves as else:
        take_input_and_parse.slow_print('\nFile does not exist. Try again.\n')

    try:
        code = open(file_name,'r',encoding='utf-8').read()

    except:
        code = open(file_name,'r',encoding='utf-16').read()

    
    if '\\' not in file_name: #if full path of file is not given
        full_name = str(pathlib.Path(__file__).parent.absolute()) + '\\' + file_name #concat the path
        print("FILE:",full_name) #informing user exactly what file is being imported and from where is important
    else:
        print("FILE:",file_name)
    
    return str(code)

def main():
    while(1):
        string = "\n\nEnter:\n1 if to pass python file.\n2 to write program here:\nq to return to quit program: "
        take_input_and_parse.slow_print(string)
        ans = input().lower()
        if ans=='1':
            code = get()
            break
            
        elif ans=='2':
            code = wants_to_type()
            break
        else:
            if ans=='q' or ans =="quit" or ans == "exit":
                take_input_and_parse.slow_print('Exiting program in ')
                for i in range(3):
                    take_input_and_parse.slow_print(str(i)+'...')
                exit()
                break
            else:                
                take_input_and_parse.slow_print("Wrong input. Try again. \n")
            
    return code


if __name__ == '__main__':
    code=main()
    take_input_and_parse.slow_print("\nRetrieved code:\n\n")
    print(code,'\n\n')
