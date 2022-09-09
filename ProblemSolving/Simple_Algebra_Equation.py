'''
Solve a given equation and return the value of 'x' in the form of a string "x=#value". The equation contains only '+', '-' 
operation, the variable 'x' and its coefficient. You should return "No solution" if there is no solution for the equation, 
or "Infinite solutions" if there are infinite solutions for the equation.

If there is exactly one solution for the equation, we ensure that the value of 'x' is an integer.

Example 1:

> Input: equation = "x+5-3+x=6+x-2"
> Output: "x=2"

Example 2:

> Input: equation = "x=x"
> Output: "Infinite solutions"

Example 3:

> Input: equation = "2x=x"
> Output: "x=0"

Constraints:

> 3 <= equation.length <= 1000
> equation has exactly one '='.
> equation consists of integers with an absolute value in the range [0, 100] without any leading zeros, and the variable 'x'

src: "https://leetcode.com/problems/solve-the-equation/"
'''

def separateExpression(expression: str) -> list[str]:

    final = []
    
    for elem in expression.split('+'):

        if elem.__contains__('-'):

            if elem[0] != '-': 

                elem = list(map(lambda x: f'-{x}', elem.split('-')))
                elem[0] = elem[0].replace('-', '+')

                final.extend(elem)

            else: final.append(elem)

        else: final.append(f'+{elem}')

    return final

def changeSign(term: str) -> str:
    return term.replace('+', '-') if term[0] == '+' else term.replace('-', '+')

def calc(coef: int, cons: int) -> str:
    return 'x={}'.format(cons / coef if (cons % coef != 0) else cons // coef) if coef != 0 else 'No solution'

def solveEquation(equation: str) -> str:

    left, right = equation.split('=')
    if (left == right): return 'Infinite solutions' 

    left_sep = list(sorted(separateExpression(left), key=lambda x: ord(x[-1])))
    right_sep = list(sorted(separateExpression(right), key=lambda x: ord(x[-1]), reverse=True))

    if (len(left_sep) == 1) and (len(right_sep) == 1):

        if ('x' in left) and ('x' in right): return 'x=0'
        elif ('x' not in left) and ('x' in right): return calc(coef=right, cons=left)

    else:

        while True:
            if left_sep[0].__contains__('x'): break
            else: right_sep.append(changeSign(left_sep.pop(0)))

            if not right_sep[0].__contains__('x'): break
            else: left_sep.append(changeSign(right_sep.pop(0)))

    left_sep = list(map(lambda x: x[0] + '1x' if len(x) == 2 else x, left_sep))
    left_coefficient = sum(map(lambda x: int(x[:-1]) if x[1] != 'x' else x.replace('x', '1x'), left_sep))
    right_constant = sum(map(int, right_sep))
            
    return calc(coef=left_coefficient, cons=right_constant)

if __name__ == '__main__': 
    
    print(solveEquation('-5+x-4x+7=99x-5+7x'))
    print(solveEquation('x+5-3+x=6+x-2'))
    print(solveEquation('-5+3=x'))
    print(solveEquation('x=-5+3'))
    print(solveEquation('x=2x'))
    print(solveEquation('3x=3x'))
    print(solveEquation('3x+2=3x'))