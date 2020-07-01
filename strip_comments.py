"""
19-05-2020: do_file function NOT WORKING CORRECTLY WHEN IMPORTED
USING OTHER MODULES. Only works correctly when this program alone
is run as a script.

FUNCTION 'do_string' is working now (correct of 28-05-20).

Program intended function:
Strip comments and docstrings from a file.
"""

def do_file(fname='user_code.py'):
    import sys, token, tokenize
    """ Run on just one file.
    """
    source = open(fname)
    mod = open("stripped_"+fname, "w")
    prev_toktype = token.INDENT
    first_line = None
    last_lineno = -1
    last_col = 0

    tokgen = tokenize.generate_tokens(source.readline)
    for toktype, ttext, (slineno, scol), (elineno, ecol), ltext in tokgen:
        if 0:   # Change to if 1 to see the tokens fly by.
            print("%10s %-14s %-20r %r" % (
                tokenize.tok_name.get(toktype, toktype),
                "%d.%d-%d.%d" % (slineno, scol, elineno, ecol),
                ttext, ltext
                ))
        if slineno > last_lineno:
            last_col = 0
        if scol > last_col:
            mod.write(" " * (scol - last_col))
        if toktype == token.STRING and prev_toktype == token.INDENT:
            # Docstring
            #mod.write("#--")
            pass
        elif toktype == tokenize.COMMENT:
            # Comment
            #mod.write("##\n")
            pass
        else:
            mod.write(ttext)
        prev_toktype = toktype
        last_col = ecol
        last_lineno = elineno

'''note: this function removes all comments and doctstrings from python program strings'''
def do_string(string):
    com_type=0
    stripped=""
    i=0
    while(i<len(string)):
        if com_type==0:
            if string[i] == "'":
                com_type=1
            elif string[i] == '"':
                com_type=2
            else:
                stripped += string[i]

        elif com_type==1:
            while(i<len(string)):
                if string[i] == "'":
                    com_type=0
                    break
                else:
                    pass
                i+=1
        else: #com_type = 2
            while(i<len(string)):
                if string[i] == '"':
                    com_type=0
                    break
                else:
                    pass
                i+=1
                
        i+=1

    return stripped

if __name__ == '__main__':
    import basic
    code = basic.get()
    stripped = do_string(code)
    print('stripped:\n'+stripped)
