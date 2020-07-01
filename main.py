import time
import take_input_and_parse
import cyclo
import lines_of_code
import basic
import feedback

def main():
    print('\n'*5)
    code=""
##    try:
    code = take_input_and_parse.main()

    fp = open('user_code.py','w')
    fp.write(code)
    fp.close()
    
    comp = cyclo.cal(code)
    take_input_and_parse.slow_print("\nCyclomatic Complexity: "+str(comp))
    LOC = lines_of_code.lines_count(code)
    take_input_and_parse.slow_print("\nLines of code (LOC):   "+str(LOC)+"\n")

    fb_cc = feedback.for_cc(comp)
    fb_loc = feedback.for_loc(LOC)
    take_input_and_parse.slow_print("\n\nFeedback:\n"+fb_cc+"\n\nExpected number of bugs based on LOC: "+fb_loc+".\n",0.005)
    
    take_input_and_parse.viewParsed(code)
    
    intro()
        
##    except:
##        basic.quit()

def intro():
    string = """\n\n\n\n\n
                    Welcome to Software Quality Evaluator for Python 3
                            by Faizan Azhar and Salman Riaz
                           Supervised by Dr. Saad Bin Saleem\n"""
    take_input_and_parse.slow_print(string,0.009)
    main()

if __name__=='__main__':
    intro()
