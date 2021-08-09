"""
Contains personal solutions to challenges.

- default-arguments
"""

# Authors: Kin-Yip Chien


class EvenStream:

    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


class OddStream:

    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


def print_from_stream(n : int, stream=EvenStream()) -> None:
    """
    Print the first *n* values returned by `get_next()` method of
    `stream` object. Each of these values values are printed on a
    separate line.

    Parameters
    ----------
    n : int
        Number of values, n, to print from `stream` object.
    stream : EvenStream or OddStream instance, default=EvenStream()
        `stream` object that returns even or odd integers through
        `get_next()` method.

    Returns
    -------
    None
    """
    stream.__init__()
    for _ in range(n):
        print(stream.get_next())


def defaultarguments() -> None:
    """
    Read an input query from STDIN where:
    * In the first line, there is a single integer *q* denoting the
        number of queries.
    * Each of the following *q* lines contains a `stream_name` followed
        by integer *n*.

    For each of the queries `(stream_name, n)`, `print_from_stream` is
    called with the appropriate `stream` object as an argument.
    """
    queries = int(input())
    for _ in range(queries):
        stream_name, n = input().split()
        n = int(n)
        if stream_name == "even":
            print_from_stream(n)
        else:
            print_from_stream(n, OddStream())
