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
1528. Shuffle String
"""
from importlib import import_module
Solution = (
    import_module(
        'problems.1528_shuffle_string')
    .Solution)
import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.soln = Solution()

    def test_restoreString(self):
        s = "codeleet"
        indices = [4, 5, 6, 7, 0, 2, 1, 3]
        self.assertEqual(
            self.soln.restoreString(s, indices), 'leetcode')

        s = "abc"
        indices = [0,1,2]
        self.assertEqual(self.soln.restoreString(s, indices), 'abc')

        s = "aiohn"
        indices = [3, 1, 4, 2, 0]
        self.assertEqual(self.soln.restoreString(s, indices), 'nihao')

        s = "aaiougrt"
        indices = [4, 0, 2, 6, 7, 3, 1, 5]
        self.assertEqual(
            self.soln.restoreString(s, indices), 'arigatou')

        s = "art"
        indices = [1, 0, 2]
        self.assertEqual(self.soln.restoreString(s, indices), 'rat')
