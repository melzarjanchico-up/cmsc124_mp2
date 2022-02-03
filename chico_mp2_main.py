"""
    FILE:       chico_mp2_main.py
    ABOUT:      Menu that contains implementations of parsing a simple expression & palindromes

    NAME:       Melzar Jan E. Chico
    COURSE:     CMSC124 B
    DATE:       2021 January 31
    TASK:       Machine Problem 2 - Syntax and Semantics
"""

from chico_mp2_one import ExpressionParser
from chico_mp2_two import PalindromeParser

def inputPrompt(gramMode):
    print(f'\t(For #{gramMode}) Input string: ', end='')
    inputStr = input()
    return inputStr

def main():
    print('Machine Problem 2: Syntax and Semantics')
    print('by Melzar Jan Chico - CMSC124B')
    grammarMode = None

    while grammarMode != '3':
        print('\nSelect between:\n\t[1] expression parsing\n\t[2] palindrome parsing\n\t[3] exit')
        print('Input selection: ', end='')

        inputString = ''
        grammarMode = input()

        if grammarMode == '1':
            print('\n\tType your strings. Type \'exit\' to go back.')
            while inputString != 'exit':
                inputString = inputPrompt(1)
                if inputString == 'exit':
                    break

                # Parser segment
                parser = ExpressionParser(inputString)
                print('\tYES, the string is in the grammar.\n' if parser.start() else '\tNO, the string is not in the grammar.\n')

        elif grammarMode == '2':
            print('\n\tType your strings. Type \'exit\' to go back.')
            while inputString != 'exit':
                inputString = inputPrompt(2)
                if inputString == 'exit':
                    break

                # Parser segment
                parser = PalindromeParser(inputString)
                print('\tThe string is A PALINDROME.\n' if parser.start() else '\tThe string is NOT A PALINDROME.\n')

        elif grammarMode == '3':
            break

        else:
            print('Invalid choice. Try again.')

main()