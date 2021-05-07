"""
Contains tests to challenges.

- py-hello-world
- py-if-else
- python-arithmetic-operators
- python-division
- python-loops
- write-a-function
- python-print
"""

# Authors: Kin-Yip Chien


# For tests.
from io import StringIO
import unittest
from unittest.mock import patch

import sys
sys.path.append('..')

from hackerrank.introduction import (
    pyhelloworld,
    pyifelse,
    pythonarithmeticoperators,
    pythondivision,
    pythonloops,
    is_leap,
    pythonprint,
)


class TestPyHelloWorld(unittest.TestCase):

    @patch('builtins.print')
    def test_pyhelloworld1(self, mock_print):
        pyhelloworld()
        mock_print.assert_called_with("Hello, World!")

    @patch('sys.stdout', new_callable=StringIO)
    def test_pyhelloworld2(self, mock_stdout):
        pyhelloworld()
        self.assertEqual(mock_stdout.getvalue(), "Hello, World!\n")


class TestPyIfElse(unittest.TestCase):

    def run_pyifelse(self, mock_input, mock_stdout):
        with patch('builtins.input', return_value=mock_input),\
                patch('sys.stdout', new_callable=StringIO) as mock_output:
            pyifelse()
            self.assertEqual(mock_output.getvalue(), mock_stdout)

    def test_pyifelse1(self):
        self.run_pyifelse('3', 'Weird\n')

    def test_pyifelse2(self):
        self.run_pyifelse('24', 'Not Weird\n')


class TestPythonArithmeticOperators(unittest.TestCase):

    def run_pythonarithmeticoperators(self, mock_input, mock_stdout):
        with patch('builtins.input', side_effect=mock_input),\
                patch('sys.stdout', new_callable=StringIO) as mock_output:
            pythonarithmeticoperators()
            self.assertEqual(mock_output.getvalue(), mock_stdout)

    def test_pythonarithmeticoperators1(self):
        self.run_pythonarithmeticoperators(['3', '5'], '8\n-2\n15\n')

    def test_pythonarithmeticoperators2(self):
        self.run_pythonarithmeticoperators(['3', '2'], '5\n1\n6\n')


class TestPythonDivision(unittest.TestCase):

    def run_pythondivision(self, mock_input, mock_stdout):
        with patch('builtins.input', side_effect=mock_input),\
                patch('sys.stdout', new_callable=StringIO) as mock_output:
            pythondivision()
            self.assertEqual(mock_output.getvalue(), mock_stdout)

    def test_pythondivision1(self):
        self.run_pythondivision(['3', '5'], '0\n0.6\n')

    def test_pythondivision2(self):
        self.run_pythondivision(['4', '3'], '1\n1.3333333333333333\n')


class TestPythonLoops(unittest.TestCase):

    def run_pythonloops(self, mock_input, mock_stdout):
        with patch('builtins.input', return_value=mock_input),\
                patch('sys.stdout', new_callable=StringIO) as mock_output:
            pythonloops()
            self.assertEqual(mock_output.getvalue(), mock_stdout)

    def test_pythonloops1(self):
        self.run_pythonloops('3', '0\n1\n4\n')

    def test_pythonloops2(self):
        self.run_pythonloops('5', '0\n1\n4\n9\n16\n')


class TestIsLeap(unittest.TestCase):

    def test_is_leap1(self):
        self.assertEqual(is_leap(1800), False)

    def test_is_leap2(self):
        self.assertEqual(is_leap(1900), False)

    def test_is_leap3(self):
        self.assertEqual(is_leap(1990), False)

    def test_is_leap4(self):
        self.assertEqual(is_leap(2000), True)

    def test_is_leap5(self):
        self.assertEqual(is_leap(2100), False)

    def test_is_leap6(self):
        self.assertEqual(is_leap(2200), False)

    def test_is_leap7(self):
        self.assertEqual(is_leap(2300), False)

    def test_is_leap8(self):
        self.assertEqual(is_leap(2400), True)

    def test_is_leap9(self):
        self.assertEqual(is_leap(2500), False)


class TestPythonPrint(unittest.TestCase):

    def run_pythonprint(self, mock_input, mock_stdout):
        with patch('builtins.input', return_value=mock_input),\
                patch('sys.stdout', new_callable=StringIO) as mock_output:
            pythonprint()
            self.assertEqual(mock_output.getvalue(), mock_stdout)

    def test_pythonprint1(self):
        self.run_pythonprint('5', '12345')

    def test_pythonprint2(self):
        self.run_pythonprint('3', '123')


if __name__ == '__main__':
    unittest.main()
