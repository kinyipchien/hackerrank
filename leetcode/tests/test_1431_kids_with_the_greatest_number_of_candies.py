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
1431. Kids With the Greatest Number of Candies
"""
from importlib import import_module
Solution = (
    import_module(
        'src.problems.1431_kids_with_the_greatest_number_of_candies')
    .Solution)
import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.soln = Solution()

    def test_kidsWithCandies(self):
        candies = [2, 3, 5, 1, 3]
        extraCandies = 3
        self.assertEqual(
            self.soln.kidsWithCandies(candies, extraCandies),
            [True, True, True, False, True])

        candies = [4, 2, 1, 1, 2]
        extraCandies = 1
        self.assertEqual(
            self.soln.kidsWithCandies(candies, extraCandies),
            [True, False, False, False, False])

        candies = [12, 1, 12]
        extraCandies = 10
        self.assertEqual(
            self.soln.kidsWithCandies(candies, extraCandies),
            [True, False, True])
