"""
Contains tests to challenges.

- np-min-and-max
- np-mean-var-and-std
- np-dot-and-cross
- np-inner-and-outer
"""

# Authors: Kin-Yip Chien


# For tests.
from io import StringIO
import unittest
from unittest.mock import patch

import sys
sys.path.append('..')

from hackerrank.hrnumpy import (
    npminandmax,
    npmeanvarandstd,
    npdotandcross,
    npinnerandouter,
)


class TestNpMinAndMax(unittest.TestCase):

    def run_npminandmax(self, mock_stdin, mock_stdout):
        with patch('sys.stdin', new=StringIO(mock_stdin)),\
                patch('sys.stdout', new_callable=StringIO) as mock_output:
            npminandmax()
            self.assertEqual(mock_output.getvalue(), mock_stdout)

    def test_npminandmax(self):
        self.run_npminandmax('4 2\n2 5\n3 7\n1 3\n4 0', '3\n')


class TestNpMeanVarAndStd(unittest.TestCase):

    def run_npmeanvarandstd(self, mock_stdin, mock_stdout):
        with patch('sys.stdin', new=StringIO(mock_stdin)),\
                patch('sys.stdout', new_callable=StringIO) as mock_output:
            npmeanvarandstd()
            self.assertEqual(mock_output.getvalue(), mock_stdout)

    def test_npmeanvarandstd(self):
        self.run_npmeanvarandstd('2 2\n1 2\n3 4', '[1.5 3.5]\n[1. 1.]\n1.11803398875\n')


class TestNpDotAndCross(unittest.TestCase):

    def run_npdotandcross(self, mock_stdin, mock_stdout):
        with patch('sys.stdin', new=StringIO(mock_stdin)),\
                patch('sys.stdout', new_callable=StringIO) as mock_output:
            npdotandcross()
            self.assertEqual(mock_output.getvalue(), mock_stdout)

    def test_npdotandcross(self):
        self.run_npdotandcross('2\n1 2\n3 4\n1 2\n3 4', '[[ 7 10]\n [15 22]]\n')


class TestNpInnerAndOuter(unittest.TestCase):

    def run_npinnerandouter(self, mock_input, mock_stdout):
        with patch('builtins.input', side_effect=mock_input),\
                patch('sys.stdout', new_callable=StringIO) as mock_output:
            npinnerandouter()
            self.assertEqual(mock_output.getvalue(), mock_stdout)

    def test_npinnerandouter(self):
        self.run_npinnerandouter(['0 1', '2 3'], '3\n[[0 0]\n [2 3]]\n')


if __name__ == '__main__':
    unittest.main()
