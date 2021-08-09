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
771. Jewels and Stones
"""
from importlib import import_module
Solution = (
    import_module('src.problems.0771_jewels_and_stones').Solution)
import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.soln = Solution()

    def test_numJewelsInStones(self):
        jewels = "aA"
        stones = "aAAbbbb"
        self.assertEqual(
            self.soln.numJewelsInStones(jewels, stones), 3)

        jewels = "z"
        stones = "ZZ"
        self.assertEqual(
            self.soln.numJewelsInStones(jewels, stones), 0)
