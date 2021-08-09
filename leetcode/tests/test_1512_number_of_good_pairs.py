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
1512. Number of Good Pairs
"""
from importlib import import_module
Solution = (
    import_module(
        'src.problems.1512_number_of_good_pairs')
    .Solution)
import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.soln = Solution()

    def test_numIdenticalPairs(self):
        nums = [1, 2, 3, 1, 1, 3]
        self.assertEqual(self.soln.numIdenticalPairs(nums), 4)

        nums = [1, 1, 1, 1]
        self.assertEqual(self.soln.numIdenticalPairs(nums), 6)

        nums = [1, 2, 3]
        self.assertEqual(self.soln.numIdenticalPairs(nums), 0)
