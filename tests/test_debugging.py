"""
Contains tests to challenges.

- default-arguments
"""

# Authors: Kin-Yip Chien


# For tests.
from io import StringIO
import unittest
from unittest.mock import patch

import sys
sys.path.append('..')

from hackerrank.debugging import (
    defaultarguments
)


class TestDefaultArguments(unittest.TestCase):

    def run_defaultarguments(self, mock_stdin, mock_stdout):
        with patch('sys.stdin', new=StringIO(mock_stdin)),\
                patch('sys.stdout', new_callable=StringIO) as mock_output:
            defaultarguments()
            self.assertEqual(mock_output.getvalue(), mock_stdout)

    def test_defaultarguments(self):
        self.run_defaultarguments('3\nodd 2\neven 3\nodd 5',
                                  '1\n3\n0\n2\n4\n1\n3\n5\n7\n9\n')


if __name__ == '__main__':
    unittest.main()
