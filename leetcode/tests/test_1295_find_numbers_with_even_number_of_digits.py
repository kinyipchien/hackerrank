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
1295. Find Numbers with Even Number of Digits
"""
from importlib import import_module
Solution = (
    import_module(
        'problems.1295_find_numbers_with_even_number_of_digits')
    .Solution)
import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.soln = Solution()

    def test_findNumbers(self):
        nums = [12, 345, 2, 6, 7896]
        self.assertEqual(self.soln.findNumbers(nums), 2)

        nums = [555, 901, 482, 1771]
        self.assertEqual(self.soln.findNumbers(nums), 1)

        nums = [999999999999999]
        self.assertEqual(self.soln.findNumbers(nums), 0)

        nums = [100000]
        self.assertEqual(self.soln.findNumbers(nums), 1)
