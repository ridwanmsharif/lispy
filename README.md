# lispy 

Interpreter for Scheme (A dialect of LISP) in Python.
Contains two modules that cover tokenizing, parsing, loading environments and evaluating valid Scheme code input.
Closely following [Peter Norvig](http://norvig.com/)'s [implementation](http://norvig.com/lispy.html) to get started. 
Covers primitive keywords and syntactic and procedure calls.
A more complete LISP interpreter is what I hope to build on top of this and I intend to closely follow Norvig's thorough [interpreter](http://norvig.com/lispy2.html). I have worked independantly to include and cover features inpired by Racket (A dialect of Scheme)
we'd been taught this past semester in CS135 at University of Waterloo.

## Coverage
Lispy is currently a lightweight interpreter that can deal with primitive and other non-primitive essentials of Scheme.
These are but not confined to the following:

+ Mathematical operators (Infix)
+ Primitive data structures (Number (Integers) , Strings, lists)
+ String literals and comments ("", ;;)
+ Procedure calls/Functions using lambda calculus
+ Abstract list functions (foldl, foldr, map, filter)
+ User defined data structures
+ Racket predicates (member?, equal?)
+ Functional paradigm supported
+ Built-in testing functions (check-expect, check-within)
+ Dynamic scoping and environment building
+ Supports algorithms designed with these restrictions
+ Command line utility so available to all users alike
+ Interactive interface with minimalistic error handling


DONE: Currently working to build procedure and evaluation definitions to support 
structures, struct functions and predicates.
The general strategy I've opted to go forward with so to avoid tampering with existing
tokenization is to identify struct commands during evaluation of parsed tokens.
Following this, I intend to use either named tuples from the collections library
or fixed length arrays with elements as fields. The idea is that any struct call to 
fields can correspond to index locations in the array.
Therefore each index location will correspond to a specefic field which will corresspond
to a 'struct-field' auto-created function. This function will act as a placeholder and 
a key in the environment and will be pushed along with its value - the index.
When this procedure is called, its lambda function will call for an array to be passed
and the index of the given array is then returned.
Thus emulating a struct in Scheme.

Lispy 3.0 has dealt with the issue vaguely described above.
However to access a field of a structure its position needs to be known. 
This position is returned by the '[struct name]-[field name]-pos'
command that is autonomously generated for every field when declaring a struct.
This is because of the structs underlying architecture I've chosen.
Examples to clarify and dispel further queries are addressed in the Examples sextion.

Memory allocation and garbage collection are handled by python's architecture.
Lispy supports an interactive environment over client's terminal as discussed below
## Setup
```sh
pip install rlispy
```
Or
```sh
git clone https://github.com/ridwanmsharif/lispy
```

## Usage

#### To begin using the environment, enter Lispy directory and run:
```sh
$ python rlispy/lis.py
```

#### Note: Enter one valid Scheme command at a time
Lispy is now ready for use:
```sh
Code: ENTER ANY SCHEME CODE HERE (NOTE THE RESTRICTIONS)
```

#### To quit the environment enter the quit command:
```sh
Code: quit
```
## Examples

#### Defining constants
```sh
Code: (define const "Constant")
Code: const
"Constant"
```

#### Defining and changing variables
```sh
Code: (define var "Variable")
Code: var
"Variable"
Code: (set! var "Variable")
Code: var
"Variable"
```

#### Basic Operations
```sh
Code: (* (+ 1 1) (/ (- 5 3) 2))
2
```

#### Defining functions and using lambda calculus
```sh
Code: (define factorial 
          (lambda (x)
              (if (<= 1)
                  1
                  (* x (factorial (- x 1))))))
Code: (factorial 5)
120
Code: (factorial 2)
2
Code: (factorial -10)
1
Code: (check-expect (factorial 3) 6)
True
Code: (check-within (factorial 3) (factorial 2) (factorial 4))
True
```

#### Using abstract list functions
```sh
Code: (define lst (list 1 2 3))
Code: lst
(1 2 3)
Code: (member? 2 lst)
True
Code: (member? 4 lst)
False
Code: (map (lambda (elem) (+ 1 elem)) lst)
(2 3 4)
Code: (foldr + 0 lst)
6
Code: (foldr (lambda (x rest) (cons x rest)) (list) lst)
(1 2 3)
Code: (foldl (lambda (x acc) (cons acc x)) (list) lst)
(3 2 1)
Code: (filter (lambda (x) (>= x 2)) lst)
(2 3)
```

#### Making use of structs
```sh
Code: (struct posn (x y z))
Code: (make-posn coordinate_a "x" "y" "z")
Code: coordinate_a
("x" "y" "z")
Code: (make-posn coornidate_fail 2 2)
TypeError: make-posn requires 3 values, given 2
Code: (posn? coordinate_a)
True
Code: (define x posn-x-pos)
Code: (define y posn-y-pos)
Code: (define z posn-z-pos)
Code: (posn-pos coordinate_a x)
"x"
Code: (posn-pos coordinate_a y)
"y"
Code: (posn-pos coordinate_a z)
"z"
```

#### Quit command to exit Lispy 3.0
```sh
Code: quit

$
```

## Disclaimer

Purely experimental project. Designed for learning purposes not production use.
Closely following [Peter Norvig](http://norvig.com/)'s [implementation](http://norvig.com/lispy.html) to get started.

## Contributing

Bug reports and pull requests are welcome on GitHub at [@ridwanmsharif](https://www.github.com/ridwanmsharif)

## Author

Ridwan M. Sharif: [E-mail](mailto:ridwanmsharif@hotmail.com), [@ridwanmsharif](https://www.github.com/ridwanmsharif)

## License

The command line utility is available as open source under the terms of
the [MIT License](https://opensource.org/licenses/MIT)


