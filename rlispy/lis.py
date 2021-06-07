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
_checkexpect = Sym('check-expect')
_checkwithin = Sym('check-within')
_member = Sym('member?')
_struct = Sym('struct')

# A prompt-read-eval-print loop.
def repl(prompt='Code: '):
    print("Lispy Version 3.0\n Get Coding!\n")
    while True:
        inpt = input(prompt)
        try:
            if inpt == "quit": break
            val = eval(parse(inpt))
            if val is not None: 
                print(schemestr(val))
        except Exception as e:
                print ('%s: %s' % (type(e).__name__, e))

# Convert a Python object back into a Scheme-readable string.
def schemestr(exp):
    if isinstance(exp, list):
        return '(' + ' '.join(map(schemestr, exp)) + ')' 
    else:
        return str(exp)

repl()
