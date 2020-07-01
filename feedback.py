"""The research for determining these ranges includes:
https://www.guru99.com/cyclomatic-complexity.html
https://docs.microsoft.com/en-us/visualstudio/python/installing-python-support-in-visual-studio?view=vs-2019

"""
import basic, cyclo

def for_cc(cc):
    if cc <=2:
        response = """Code:           Perfectly flat. Can be used in any environment.
Testability:    Very High.
Cost & Effort:  Negligible."""
        return response
    
    if cc>2 and cc<10:
        response = """Code:           Not complex. Well structured, well written.
Testability:    High.
Cost & Effort:  Minimal."""
        return response
    
    if cc>=10 and cc<20:
        response = """Code:           Complex. 
Testability:    Medium.
Cost & Effort:  Medium."""
        return response
    
    if cc>=20 and cc<30:
        response = """
Code:           Very Complex. If you're a beginner-intermediate programmer,
                please consider redesigning architecture.

Testability:    Low.
Cost & Effort:  Medium."""
        return response

    if cc>=30 and cc<40:
        response = """
Code:           ALARMINGLY COMPLEX! Approaching extremely low maintanability.
                Only consider using this as standalone script, not as a module in a project.

Testability:    Very Low.
Cost & Effort:  Very High."""
        return response
        
    if cc>=40:
        response = """
Code:           NOT MAINTAINABLE AT ALL! DO NOT USE THIS AS A MODULE UNDER ANY CIRCUMSTANCES!
                COMPLETE REDESIGN RECOMMENDED!

Testability:    NOT AT ALL TESTABLE!
Cost & Effort:  ALARMINGLY HIGH!"""
        return response

def for_loc(n):
    """
    This function returns number of expected bugs in a python program
    based on the lines of code. ]

    This information is based on Table 1 from “Analysis of complexity
    metrics of a software code for obfuscating transformations of an
    executable code” (Kuznetsov, 2016)

    However it is only for the first 5000 lines of code, as we plan on
    limiting size of input code to avoid crashes.
    """
    if n>=0 and n<10:
        return '0'
    
    if n>=10 and n<100:
        return '1-4'

    if n>=100 and n<200:
        return '5-9'

    if n>=200 and n<300:
        return '10-13'

    if n>=300 and n<400:
        return '14-17'

    if n>=400 and n<500:
        return '18-21'

    if n>=500 and n<600:
        return '22-24'

    if n>=600 and n<700:
        return '25-27'

    if n>=700 and n<800:
        return '28-30'

    if n>=800 and n<900:
        return '31-33'

    if n>=900 and n<1000:
        return '34-36'

    if n>=1000 and n<2000:
        return '37-70'

    if n>=3000 and n<4000:
        return '71-105'

    if n>=4000 and n<5000:
        return '106-140'

    if n>=5000:
        return '>150'

if __name__ == '__main__':
    code = basic.get()
    cc = cyclo.cal(code)
    print(for_cc(cc))
