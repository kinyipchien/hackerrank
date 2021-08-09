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
1089. Duplicate Zeros
"""
from importlib import import_module
Solution = (import_module('problems.1089_duplicate_zeros')
            .Solution)
import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.soln = Solution()

    def test_duplicateZeros(self):
        arr = [1, 0, 2, 3, 0, 4, 5, 0]
        self.soln.duplicateZeros(arr)
        self.assertEqual(arr, [1, 0, 0, 2, 3, 0, 0, 4])

        arr = [1, 2, 3]
        self.soln.duplicateZeros(arr)
        self.assertEqual(arr, [1, 2, 3])
