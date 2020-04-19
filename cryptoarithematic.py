import string, re, itertools

def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    compile_word('YOU')
    for f in fill_in(formula):
        if valid(f):
            return f
    
def fill_in(formula):
    "Generate all possible fillings-in of letters in formula with digits."
    # english_letters = (ch for ch in formula if ch.isalpha())
    english_letters = re.findall('[A-Z]', formula)
    letters = ''.join(set(english_letters)) #should be a string
    for digits in itertools.permutations('1234567890', len(letters)):
        table = string.maketrans(letters, ''.join(digits))
        yield formula.translate(table)
    
def valid(f):
    """Formula f is valid if and only if it has no 
    numbers with leading zero, and evals true."""
    try: 
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    # Your code here.
    #better solution
    if not word.isupper():
        return word
    else:
        compiled_word = [ ('%s*%s' %(10**i, ch))
                            for i, ch in enumerate(word[::-1]) ]
    new_word =  '(' + '+'.join(compiled_word) + ')'
    print new_word
    return new_word


    #my solution
    # compiled_word = []
    # power = 0;
    # if not word.isupper():
    #     return word

    # for i,ch in enumerate(word[::-1]): #from the back
    #     if not ch.isalpha:
    #         compiled_word.append(ch)
    #     else:
    #         form = str(10**i) + '*' + ch
    #         compiled_word.append(form)
    
    # compiled_word = '(' + '+'.join(compiled_word) + ')'
    # print compiled_word

    # return compiled_word


if __name__ == "__main__":
    solve('A + B == C**2')