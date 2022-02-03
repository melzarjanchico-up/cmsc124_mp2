#   FILE:       chico_mp2_one.py
#   ABOUT:      A class that does parsing for the following specifications:
#               simple expressions limited to the variable identifiers x, y, 
#               or z, that contain the operations of addition (+), subtraction (-), 
#               and unary negation (~) together with parentheses.
#
#   NAME:       Melzar Jan E. Chico
#   COURSE:     CMSC124 B
#   DATE:       2021 January 31
#
#   TASK:       Machine Problem 3 - Lexical and Syntax Analysis (No. 1)
#   NOTICE:     Here's the BNF grammar given from MP1 No.1:
#                   <exp>   ::= <exp><op><exp> | (<exp>) | ~<exp> | <id>
#                   <id>    ::= x | y | z
#                   <op>    ::= + | -
#               But I have to convert to LL form to be able to parse it:
#                   <exp>   ::= (<exp>)<exp'> | ~<exp><exp'> | <id><exp'>
#                   <exp'>  ::= <op><exp><exp'> | e
#                   <id>    ::= x | y | z
#                   <op>    ::= + | -

class ExpressionParser:
    def __init__(self, strLine) -> None:
        self.__strLine = strLine
        self.__currChar = None
        self.__currPos = -1
        self.__isError = False
        self.nextChar()

    def nextChar(self):
        self.__currPos += 1

        if self.__currPos >= len(self.__strLine):
            # Forced '$' incase user forgot the dollar sign
            self.__currChar = '$'
        else:
            self.__currChar = self.__strLine[self.__currPos]

    def match(self, char):
        return self.__currChar == char

    def start(self):
        self.expression()

        # Checks if the parser read the string entirely
        if not self.match('$') or (self.match('$') and self.__currPos < len(self.__strLine)-1):
            self.__isError = True

        return (True if not self.__isError else False)

    ### GRAMMAR STARTS HERE ###

    def expression(self):
        if self.match('('):                     # <exp> ::= (<exp>)<exp'>
            self.nextChar()
            self.expression()
            if self.match(')'):
                self.nextChar()
            else:
                self.__isError = True
            self.expression_prime()

        elif self.match('~'):                   # <exp> ::= ~<exp><exp'>
            self.nextChar()
            self.expression()
            self.expression_prime()

        elif self.__currChar in ['x','y','z']:  # <exp> ::= <id><exp'> (could be self.identifier(), but it's redundant)
            self.nextChar()
            self.expression_prime()
        
        else:
            self.__isError = True

    def expression_prime(self):
        if self.__currChar in ['+','-']:        # <exp'> ::= <op><exp><exp'> (could be self.operator(), but it's redundant
            self.nextChar()
            self.expression()
            self.expression_prime()

        else:                                   # <exp'> ::= e (this can be removed too, just added this for clarity)
            pass