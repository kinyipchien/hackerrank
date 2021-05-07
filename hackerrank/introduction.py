"""
Contains personal solutions to challenges.

- py-hello-world
- py-if-else
- python-arithmetic-operators
- python-division
- python-loops
- write-a-function
- python-print
"""

# Authors: Kin-Yip Chien


def pyhelloworld() -> None:
    """
    Print `Hello, World!` to stdout.

    Parameters
    ----------
    None

    Returns
    -------
    None

    Examples
    --------
    >>> pyhelloworld()
    Hello, World!
    """
    print("Hello, World!")


def pyifelse() -> None:
    """
    Given an integer, *n*, perform the following conditional actions:

    * If *n* is odd, print `Weird`
    * If *n* is even and in the inclusive range of **2** to **5**,
        print `Not Weird`
    * If *n* is even and in the inclusive range of **6** to **20**,
        print `Weird`
    * If *n* is even and greater than **20**, print `Not Weird`

    Parameters
    ---------
    None

    Returns
    -------
    None
    """
    n = int(input().strip())
    if n % 2 == 1:
        print('Weird')
    elif n in range(2, 5 + 1):
        print('Not Weird')
    elif n in range(6, 20 + 1):
        print('Weird')
    elif n > 20:
        print('Not Weird')


def pythonarithmeticoperators() -> None:
    """
    Read two integers from STDIN, *a* and *b* and print three lines
    where:

    1. The first line contains the sum of the two numbers.
    2. The second line contains the difference of the two numbers.
    3. The third line contains the product of the two numbers.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)


def pythondivision() -> None:
    """
    Read two integers, *a* and *b*, from STDIN and print two lines. The
    first line contains the result of integer division, *a*//*b*. The
    second line contains the result of float division, *a*/*b*.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)


def pythonloops() -> None:
    """
    Read an integer, *n*, from STDIN. For all non-negative integers *i*
    < *n*, print :math:`i^2`.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    n = int(input())
    for i in range(n):
        print (i**2)


def is_leap(year: int) -> bool:
    """
    Determine whether a year is a leap year.

    Parameters
    ----------
    year : int
        Year.

    Returns
    -------
    leap : bool
        Whether `year` is a leap year.

    Notes
    -----
    In the Gregorian calendar, three conditions are used to identify
    leap years:

    * The year can be evenly divided by 4, is a leap year, unless:
        * The year can be evenly divided by 100, it is NOT a leap year,
            unless:
            * The year is also evenly divisible by 400. Then it is a
              leap year.

    Examples
    --------
    >>> is_leap(2000)
    True
    >>> is_leap(1800)
    False
    """
    leap = False

    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True

    return leap


def pythonprint() -> None:
    """
    Read an integer, *n*, from STDIN and print the following:

    **123...n**

    where "..." represents the consecutive values in between.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    n = int(input())
    for i in range(1, n + 1):
        print(i, end='')
