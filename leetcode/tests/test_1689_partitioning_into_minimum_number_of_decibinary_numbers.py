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
1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
"""
from importlib import import_module
Solution = (
    import_module(
        'src.problems.1689_partitioning_into_minimum_number_of_decibinary_numbers')
    .Solution)
import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.soln = Solution()

    def test_minPartitions(self):
        n = "32"
        self.assertEqual(self.soln.minPartitions(n), 3)

        n = "82734"
        self.assertEqual(self.soln.minPartitions(n), 8)

        n = "27346209830709182346"
        self.assertEqual(self.soln.minPartitions(n), 9)
