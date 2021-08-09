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
1720. Decode XORed Array
"""
from importlib import import_module
Solution = (
    import_module(
        'problems.1720_decode_xored_array')
    .Solution)
import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.soln = Solution()

    def test_decode(self):
        encoded = [1, 2, 3]
        first = 1
        self.assertEqual(
            self.soln.decode(encoded, first), [1, 0, 2, 1])

        encoded = [6, 2, 7, 3]
        first = 4
        self.assertEqual(
            self.soln.decode(encoded, first), [4, 2, 0, 7, 4])
