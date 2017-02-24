# lispy (Python)

Interpreter for Scheme (A dialect of LISP) in Python.
Contains two modules that cover tokenizing, parsing, loading environments and evaluating valid Scheme code input.
Closely following [Peter Norvig](http://norvig.com/)'s [implementation](http://norvig.com/lispy.html) to get started. 
Covers primitive keywords and syntactic and procedure calls.
A more complete LISP interpreter is what I hope to build on top of this and I intend to closely follow Norvig's thorough [interpreter](http://norvig.com/lispy2.html) to account for all the missing calls.
Those include but are not confined to: Data Structures, Macros, error detection, call/cc, syntax and more.

For now, lispy can deal with primitive and abstract functions, mathematical operations, primitive data structures (Number, Strings, lists) and supports algorithms designed with these restrictions.
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

To begin using the environment, enter Lispy directory and run:
```sh
$ python rlispy/lis.py
```

Note: Enter one valid Scheme command at a time
Lispy is now ready for use:
```sh
Code: ENTER ANY SCHEME CODE HERE (NOTE THE RESTRICTIONS)
```

To quit the environment enter the quit command:
```sh
Code: quit
```
## Examples
Defining constants
```sh
Code: (define const 1)
Code: const
1
```

Defining and changing variables
```sh
Code: (define var 1)
Code: var
1
Code: (set! var 2)
Code: var
2
```

Basic Operations
```sh
Code: (* (+ 1 1) (/ (- 5 3) 2))
2
```

Lets have some fun shall we.
Defining functiona and using lambda calculus
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
```

Good enough for now? Alright then
```sh
Code: quit

$ sudo go-about-your-business-now
```

## Disclaimer

Purely experimental project. Designed for learning purposes not production use.
Closely following [Peter Norvig](http://norvig.com/)'s [implementation](http://norvig.com/lispy.html) to get started.

## Contributing

Bug reports and pull requests are welcome on GitHub at [@ridwanmsharif](https://www.github.com/ridwanmsharif)

## Author

Ridwan M. Sharif: [E-mail](ridwanmsharif@hotmail.com), [@ridwanmsharif](https://www.github.com/ridwanmsharif)

## License

The command line utility is available as open source under the terms of
the [MIT License](https://opensource.org/licenses/MIT)

