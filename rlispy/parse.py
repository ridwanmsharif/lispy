# Parsing Module

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

# A Scheme Symbol is implemented as a Python str
# A Scheme List is implemented as a Python list
# A Scheme Number is implemented as a Python int or float
Symbol = str
List   = list
Number = (int, float)

