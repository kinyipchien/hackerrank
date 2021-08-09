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
1365. How Many Numbers Are Smaller Than the Current Number
"""
from importlib import import_module
Solution = (
    import_module(
        'problems.1365_how_many_numbers_are_smaller_than_the_current_number')
    .Solution)
import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.soln = Solution()

    def test_smallerNumbersThanCurrent(self):
        nums = [8, 1, 2, 2, 3]
        self.assertEqual(
            self.soln.smallerNumbersThanCurrent(nums), [4, 0, 1, 1, 3])

        nums = [6, 5, 4, 8]
        self.assertEqual(
            self.soln.smallerNumbersThanCurrent(nums), [2, 1, 0, 3])

        nums = [7,7,7,7]
        self.assertEqual(
            self.soln.smallerNumbersThanCurrent(nums), [0, 0, 0, 0])
