from eval import *

_quote = Sym('quote')
_if = Sym('if')
_set = Sym('set!')
_define = Sym('define')
_lambda = Sym('lambda')
_begin = Sym('begin')
_definemacro = Sym('define-macro')
_quasiquote = Sym('quasiquote')
_unquoto = Sym('unquote')
_unquotesplicing = Sym('unquote-splicing')

# A prompt-read-eval-print loop.
def repl(prompt='Code: '):
    print("Lispy Version 2.0\n Get Coding!\n")
    while True:
        inpt = raw_input(prompt)
        try:
            if inpt == "quit": break
            val = eval(parse(inpt))
            if val is not None: 
                print(schemestr(val))
        except Exception as e:
                print '%s: %s' % (type(e).__name__, e)

# Convert a Python object back into a Scheme-readable string.
def schemestr(exp):
    if isinstance(exp, list):
        return '(' + ' '.join(map(schemestr, exp)) + ')' 
    else:
        return str(exp)

repl()
