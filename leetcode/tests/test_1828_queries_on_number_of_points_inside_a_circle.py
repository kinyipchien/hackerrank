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
1828. Queries on Number of Points Inside a Circle
"""
from importlib import import_module
Solution = (
    import_module(
        'problems.1828_queries_on_number_of_points_inside_a_circle')
    .Solution)
import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.soln = Solution()

    def test_countPoints(self):
        points = [[1, 3], [3, 3], [5, 3], [2, 2]]
        queries = [[2, 3, 1], [4, 3, 1], [1, 1, 2]]
        self.assertEqual(
            self.soln.countPoints(points, queries), [3, 2, 2])

        points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
        queries = [[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]]
        self.assertEqual(
            self.soln.countPoints(points, queries), [2, 3, 2, 4])
