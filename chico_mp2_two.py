#   FILE:       chico_mp2_one.py
#   ABOUT:      A class that does parsing for palindromes
#
#   NAME:       Melzar Jan E. Chico
#   COURSE:     CMSC124 B
#   DATE:       2022 January 31
#
#   TASK:       Machine Problem 3 - Lexical and Syntax Analysis (No. 2)
#   NOTICE:     Here's the BNF grammar given from MP1 No.2:
#                   <pal> ::= a | ... | z | a<pal>a | ... | z<pal>z | e
#
#               Creating a topdown parser for palindromes is impossible due to reasons
#               of not knowing when to apply non-recursive productions without knowledge
#               the maximum input length of the strings (rici, 2020). Hence, the
#               implementation belows just checks for a string if it is a palindrome 
#               using a simple recursion & a reversed version of the string.
#               
#   CREDITS:    rici (April 2020). Stackoverflow. Retrieved from https://stackoverflow.com/questions/61417389/bison-flex-practicing-with-the-language-of-palindrome-strings

class PalindromeParser:
    def __init__(self, strLine:str) -> None:
        self.__strLine = strLine.replace(" ","").lower()
        self.__strLineRev = self.__strLine[::-1]
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
        if self.__currChar.isalpha() and self.match(self.__strLineRev[self.__currPos]):
            self.nextChar()
            self.expression()