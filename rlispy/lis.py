from eval import *

# A prompt-read-eval-print loop.
def repl(prompt='Code: '):
    while True:
        inpt = raw_input(prompt)
        if inpt == "quit": break
        val = eval(parse(inpt))
        if val is not None: 
            print(schemestr(val))

# Convert a Python object back into a Scheme-readable string.
def schemestr(exp):
    if isinstance(exp, List):
        return '(' + ' '.join(map(schemestr, exp)) + ')' 
    else:
        return str(exp)

repl()
