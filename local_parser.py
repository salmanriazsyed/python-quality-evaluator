'''
This program safely attempts to parse code and return the parsed tree module
if successful. Returns None type object in case of failure.
'''

import ast

def attempt(code):
    try:
        if code[-1]=='$': #in case of taking program input from user directly
            parsed = parse_tree(code[0:-1]) #try parsing the code
        elif code[-2]=='$':
            parsed = parse_tree(code[0:-2]) #parse till $
        else:
            try:
                parsed = parse_tree(code) #parse entire code
            except:
                print("\nERROR: Faulty program entered.\n")
        return ast.dump(parsed)

    except: #in case of failure
        print("\nError in parser.py : User has entered faulty program.\n")
        return 

def abstract_syntax(code):
    tree = parse_tree(code)
    string_tree = ""
    for obj in ast.walk(tree):
        string_tree = string_tree + str(type(obj))+ '\n'
    return string_tree

def parse_tree(code):
    try:
        return ast.parse(code)
    except:
        print("\nFaulty program entered.\n")
        return

if __name__ == '__main__':
    import basic
    code = basic.main()
    print('Parsed:\n\n',attempt(code))
