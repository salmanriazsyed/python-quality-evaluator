'''
This program extracts python functions from python programs and allows single line insertion
of code in them.

Module used: Python built-in 'inspect'.
https://docs.python.org/3/library/inspect.html
'''
import ast
import inspect
import os
import basic

def extract(code):
    try:
        parsed = ast.parse(code)
    except:
        print('\nParsing failed in module: function_manipulation. Faulty code.')
        return

    functions = []
    for obj in ast.walk(parsed): #walk over each module of parsed tree
        if str(type(obj))=="<class '_ast.FunctionDef'>": #look for function object
            functions.append(obj)

    for i in range(len(functions)):
        source_func = inspect.getsourcelines(functions[i]) #returns a list of lines from func object
        print('\n\nFunction',i,':\n',source_func)


if __name__ == '__main__':
    code = basic.get()
    extract(code)
