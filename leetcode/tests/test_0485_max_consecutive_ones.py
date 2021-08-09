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
485. Max Consecutive Ones
"""
from importlib import import_module
Solution = import_module('problems.0485_max_consecutive_ones').Solution
import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.soln = Solution()

    def test_findMaxConsecutiveOnes(self):
        nums = [1, 1, 0, 1, 1, 1]
        self.assertEqual(self.soln.findMaxConsecutiveOnes(nums), 3)

        nums = [1, 0, 1, 1, 0, 1]
        self.assertEqual(self.soln.findMaxConsecutiveOnes(nums), 2)