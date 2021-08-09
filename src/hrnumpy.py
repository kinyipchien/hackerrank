"""
Contains personal solutions to challenges.

- np-min-and-max
- np-mean-var-and-std
- np-dot-and-cross
- np-inner-and-outer
"""

# Authors: Kin-Yip Chien


import numpy


def npminandmax() -> None:
    """
    Given a 2-D array with dimensions *N*X*M*, print the max of the min
    function over axis **1**.

    Parameters
    ----------
    None

    Returns
    -------
    None

    Notes
    -----
    The first line of input contains the space separated values of *N*
    and *M*.
    The next *N* lines containes *M* space separated integers.
    """
    N, M = map(int, input().split())
    arr = numpy.array([input().split() for _ in range(N)], int)
    print(arr.min(axis=1).max())


def npmeanvarandstd() -> None:
    """
    Given a 2-D array of size ***N***X***M***, prints 3 lines:
    1. The mean along axis **1**
    2. The var along axis **0**
    3. The std along axis ***None***

    Parameters
    ----------
    None

    Returns
    -------
    None

    Notes
    -----
    The first line of input contains the space separated values of
    ***N*** and ***M***.
    The next ***N*** lines contain ***M*** space separated integers.
    """
    N, M = map(int, input().split())
    arr = numpy.array([input().split() for _ in range(N)], int)
    print(arr.mean(axis=1))
    print(arr.var(axis=0))
    print(arr.std().round(11))


def npdotandcross() -> None:
    """
    Given two arrays ***A*** and ***B***, both with dimensions
    ***N***X***N***, prints the matrix multiplication of ***A*** and
    ***B***.

    Parameters
    ----------
    None

    Returns
    -------
    None

    Notes
    -----
    The first line of input contains the integer ***N***.
    The next ***N*** lines contain ***N*** space separated integers of
    array ***A***.
    The following ***N*** lines contain ***N*** space separated
    integers of array ***B***.
    """
    N = int(input())
    A = numpy.array([input().split() for _ in range(N)], int)
    B = numpy.array([input().split() for _ in range(N)], int)
    print(A @ B)


def npinnerandouter() -> None:
    """
    Given two arrays ***A*** and ***B***, print 2 lines:
    1. The inner product.
    2. The outer product.

    Parameters
    ----------
    None

    Returns
    -------
    None

    Notes
    -----
    The first line of input contains the space separated elements of
    array ***A***.
    The second line of input contains the space separated elements of
    array ***B***.
    """
    A = numpy.array(input().split(), int)
    B = numpy.array(input().split(), int)
    print(numpy.inner(A, B))
    print(numpy.outer(A, B))
