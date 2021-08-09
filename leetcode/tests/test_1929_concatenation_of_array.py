# Copyright (C) 2021  Kin-Yip Chien

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
1929. Concatenation of Array
"""
from importlib import import_module
Solution = (
    import_module(
        'src.problems.1929_concatenation_of_array')
    .Solution)
import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.soln = Solution()

    def test_getConcatenation(self):
        nums = [1, 2, 1]
        self.assertEqual(
            self.soln.getConcatenation(nums), [1, 2, 1, 1, 2, 1])

        nums = [1, 3, 2, 1]
        self.assertEqual(
            self.soln.getConcatenation(nums), [1, 3, 2, 1, 1, 3, 2, 1])
