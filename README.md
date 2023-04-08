# Computer Science and Programming in Python



## 1. Topics

- Represent knowledge with data structure
- Iteration and recursion as computational metaphors
- Abstraction of procedures and data types
- Organize and modulative systems using object classes and methods
- Different classes of algorithms, searching and sorting
- Complexity of algorithms



## 2. Objects

Programs manipulate data objects

- Objects are

  - Scalar (connot be subdivided)

  - Non-scalar (have internal structure that can be accessed)

- Scalar objects
  - int
  - float
  - bool
  - NoneType - special and has one value, None
  - can use type() to see the type of an object


## 3. Contents

- Branching and Iteration

  - strings
  - branching - if/elif/else
  - while loops
  - for loops

- Sring manipulation guess-and-check approximations bisection

  - string manipulation
  - guess and check algorithms (exhaustive enumeration)
  - approximate solutions (start with a guess and increment by some small value)
  - bisection method (half interval each iteration, new guess is halfway in between)

- Structuring programs and hiding details

  - projectors and decomposition
  - abstraction
  - functions and scope

- Tuplea, lists, aliasing, mutability, cloning

  - compound data types: tuples and lists
    - tuples: immutable, swap variables values, return more than one value from a function
    - lists-mutable
  - idea of aliasing
  - idea of mutability
  - idea of cloning

- Recursion , dictionary

  - recursion-divide/decrease and conquer

    recursion is the process of repeating items in a self-similar way

    - reduce a problem to simpler versions of the same problem
    - must have one or more base cases that are easy to solve
    - must solve the same problem on some other input with the goal of simplifying the larger problem input
    - examples: multiplication iterative, factorial
      - each recursive call to a function creates its own scope/environment
      - bindings of variables in a scope are not changed by recursive call
      - flow of control passes back to previous scope once function call returns value

  - dictionaties-another mutable object type

    - values
      - any type
      - can be duplicates
      - dictionary values can be lists, even other dictionaries
    - keys
      - must be unique
      - immutable type
    - no order to keys or values
