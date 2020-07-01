"""
Huge thanks to Sanjay Misra and Ferid Cafer for breaking down the computation of complexity metrics
into easily readable tables. They formulated their own complexity metric for object oriented languages
and for its implementation they broke their diagram down into a few steps. For one of those steps
they created a table in which an encountered object/statement is directly presented with the number
it adds to the overall complexity. Their metric is called SMPy (Software Metric for Python).
This metric along with the tables can be found in the following paper:
'ESTIMATING COMPLEXITY OF PROGRAMS IN PYTHON LANGUAGE by Sanjay Misra, Ferid Cafer. ISSN: 1330-3651'


Coming back to this project, this idea of breaking diagrams down into tables that are essentially
explaining the same idea makes the implementation of such metrics in programs not only easier and
more readable, but also very well optimized, compared to other programs that compute cyclomatic
complexity for python programs.

The main difference between the process between this project and other libraries such as radon and mccabe
is that in those libraries, after going over objects, a control flow graph is implemented in the
background before any calculation is done. This control flow diagram can also be displayed with those
libraries. This function comes in handy in situations where the purpose of software is to directly
display the working of a program (with the goal being helping reduce its complexity).
Although, the goal of this project is rooted in the same motivation, the implementation can be
altered to make it better suited for this project.

The purpose of this project (past its academic phase) is to provide the numbers along with
code suggestions to help reduce program complexity, we do not need to create an entire control flow graph.


Now onto the technical explanation:

Since we know that the formula of cyclomatic complexity (McCabe complexity) = Edges - Nodes + 2.
What we can do is count the number of edges and nodes each type of 'branching' statement adds to the
control flow graph. In that manner we have to neither draw it, nor complete it prior to calculations.
It really keeps our project focused on the quality evaluation part and helps keep it well optimized.
Using McCabes Complexity formula, this is what the computation breaks down into:

 ___________________________________________________________________________________
|                           |           |           |                               |
|                           |           |           |                               |
|       Object/Statement    |   Edges   |   Nodes   |       McCabe Complexity       |
|                           |           |           |                               |
|___________________________|___________|___________|_______________________________|
|                           |           |           |                               |
|                           |           |           |                               |
|                           |           |           |                               |
|              If           |     2     |     3     |   McCabe = 2 - 3 + 2 = 1      |
|                           |           |           |                               | 
|                           |           |           |                               |
|                           |           |           |                               |
|___________________________|___________|___________|_______________________________|
|                           |           |           |                               |
|                           |           |           |                               |
|                           |           |           |                               |
|             For           |     3     |     3     |   McCabe = 3 - 3 + 2 = 2      |
|                           |           |           |                               |
|                           |           |           |                               |
|                           |           |           |                               |
|___________________________|___________|___________|_______________________________|
|                           |           |           |                               |
|                           |           |           |                               |
|                           |           |           |                               |
|            While          |     3     |     3     |   McCabe = 3 - 3 + 2 = 2      |
|                           |           |           |                               |
|                           |           |           |                               |
|                           |           |           |                               |
|___________________________|___________|___________|_______________________________|
|                           |           |           |                               |
|                           |           |           |                               |
|                           |           |           |                               |
|         Comprehension     |     3     |     3     |   McCabe = 3 - 3 + 2 = 2      |
|                           |           |           |                               |
|                           |           |           |                               |
|                           |           |           |                               |
|___________________________|___________|___________|_______________________________|
|                           |           |           |                               |
|                           |           |           |                               |
|                           |           |           |                               |
|              Try          |     2     |     3     |   McCabe = 2 - 3 + 2 = 1      |
|                           |           |           |                               |
|                           |           |           |                               |
|                           |           |           |                               |
|___________________________|___________|___________|_______________________________|
|                           |           |           |                               |
|                           |           |           |                               |
|                           |           |           |                               |
|              With         |     1     |     2     |   McCabe = 1 - 2 + 2 = 1      |
|                           |           |           |                               |
|                           |           |           |                               |
|                           |           |           |                               |
|___________________________|___________|___________|_______________________________|
|                           |           |           |                               |
|                           |           |           |                               |
|                           |           |           |                               |
|              Assert       |     2     |     3     |   McCabe = 2 - 3 + 2 = 1      |
|                           |           |           |                               |
|                           |           |           |                               |
|                           |           |           |                               |
|___________________________|___________|___________|_______________________________|

Summary: This program uses python's builtin AST module to walk over the input program's parsed tree to
identify branching nodes ( conditions / loops / try etc. ) Without having to count all the edges and nodes and then
computing cyclomatic complexity, the table drawn above provides solution in the way that on identification of each
of these branching nodes, we add numbers to the complexity as given in the table.
This table has been derrived from the Mccabe complexity formula E - N + 2.
"""

import ast
import os
import local_parser
import basic

def cal(code):
    try:
        tree = local_parser.parse_tree(code)
        complexity = 1 #each program has a one path of execution minimum

        #check=0
        """
           This implementation of boolean expressions has been removed from the
           program as well as the table as in python language multiple boolean
           expressions are used in if conditions however they do not add any
           paths in a program. The idea was originally taken from radon library's
           implementation however after some research and testing, it was found
           that these do not add to the complexity. Radon has only implemented their
           own version of complexity which is why they add a value against boolean
           expressions. Our goal is to keep this project as close to the original
           mccabe complexity as possible, so that it corresponds directly to the
           quality of a program and not test cases only. This can be seen as a
           limitation by computing complexity in this optimized fashion as well.


           Old ocmment explaining how boolean was implemented to work with
           if conditions:
           
           When walking over the tree, an if condition is followed by a Boolean
           expression, for readability's sake we keep that as if condition in
           the table, however the boolean expression has to not add anything
           in such positions to the complexity, hence we use this check flag."""
        
        for i in ast.walk(tree):

            """Note: elif statement is also recongized as a class type 'If' object in
               python when parsed with ast module."""

            if str(type(i))=="<class '_ast.If'>": #object type wrt table 'If' condition.
                complexity+=1
                #check=1
                continue

            if str(type(i))=="<class '_ast.For'>": #object type wrt table 'For'.
                complexity+=2
                #check=0
                continue


            """Note: In python, the implementation of do while is the same as while
               so we do not need to put another identification in place for do while"""
            
            if str(type(i))=="<class '_ast.While'>": #object type wrt table 'While'.
                complexity+=2
                #check=1
                continue

            if str(type(i))=="<class '_ast.Try'>": #object type wrt table 'Try'.
                complexity+=1
                #check=0
                continue

            """
            Past the project's academic phase, this will be integrated as well, however with a
            different approach based on research and empirical testing. Depending on how
            many boolean operators are found in a program, a number will be added to the
            complexity, however this will not be cyclomatic complexity as we want to
            keep the CC implementation as close to the original metric as possible.
            
            if str(type(i))=="<class '_ast.Compare'>": #object  type wrt table 'Boolean'. 
                if check==0:
                    complexity+=1
                    continue
                else:
                    check=0
                    continue
            """
            
            if str(type(i))=="<class '_ast.With'>": #object type wrt table 'With' 
                complexity+=1
                #check=0
                continue

            if str(type(i))=="<class '_ast.ListComp'>": #object type (list comprehensions) wrt table 'Comprehension' 
                complexity+=2
                #check=0
                continue

            if str(type(i))=="<class '_ast.SetComp'>": #object type (set comprehensions) wrt table 'Comprehension' 
                complexity+=2
                #check=0
                continue

            if str(type(i))=="<class '_ast.DictComp'>": #object type (dictionary comprehensions) wrt table 'Comprehension' 
                complexity+=2
                #check=0
                continue
            


            if str(type(i))=="<class '_ast.Assert'>": #object type wrt table 'Comprehension' 
                complexity+=1
                #check=0

        return complexity

    except:
        print("Message from cyclo.py: Faulty program entered.")

if __name__ == '__main__':
    code = basic.get()
    print("Complexity: ",cal(code), '.',sep='')
