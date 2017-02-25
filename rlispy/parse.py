# Parsing Module

from __future__ import division
import re, sys, StringIO

# A Scheme List is implemented as a Python list
# A Scheme Number is implemented as a Python int or float
Symbol = str
List   = list
Number = (int, float)

# Class for LISP common symbols
class _Symbol(str): pass

symbol_table = {}

# Find or create unique Symbol entry for str s in symbol table
def Sym(s):
    if s not in symbol_table: 
        symbol_table[s] = Symbol(s)
    return symbol_table[s]

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

# Tokenize input string.
def tokenize(code):
    return code.replace('(', ' ( ').replace(')', ' ) ').split()

# Read an expression from a sequence of tokens.
def read_from_tokens(tokens):
    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF while reading')
    token = tokens.pop(0)
    if '(' == token:
        L = []
        while tokens[0] != ')':
            L.append(read_from_tokens(tokens))
        tokens.pop(0)
        return L
    elif ')' == token:
        raise SyntaxError('unexpected )')
    else:
        return atom(token)

# Numbers become numbers; every other token is a symbol.
def atom(token):
    try: return int(token)
    except ValueError:
        try: return float(token)
        except ValueError:
            return Symbol(token)

# Read a Scheme expression from a string.
def parse(code):
    return read_from_tokens(tokenize(code))

