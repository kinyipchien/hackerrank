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
1476. Subrectangle Queries
"""
from importlib import import_module
SubrectangleQueries = (
    import_module(
        'problems.1476_subrectangle_queries')
    .SubrectangleQueries)
import unittest


class TestSubrectangleQueries(unittest.TestCase):

    def setUp(self):
        self.input = [
            [
                ["SubrectangleQueries",
                 "getValue",
                 "updateSubrectangle",
                 "getValue",
                 "getValue",
                 "updateSubrectangle",
                 "getValue",
                 "getValue"],
                [[[[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]]],
                 [0, 2],
                 [0, 0, 3, 2, 5],
                 [0, 2],
                 [3, 1],
                 [3, 0, 3, 2, 10],
                 [3, 1],
                 [0, 2]]
            ],
            [
                ["SubrectangleQueries",
                 "getValue",
                 "updateSubrectangle",
                 "getValue",
                 "getValue",
                 "updateSubrectangle",
                 "getValue"],
                [[[[1, 1, 1], [2, 2, 2], [3, 3, 3]]],
                 [0, 0],
                 [0, 0, 2, 2, 100],
                 [0, 0],
                 [2, 2],
                 [1, 1, 2, 2, 20],
                 [2, 2]]
            ]
        ]
        self.expected = [
            [None, 1, None, 5, 5, None, 10, 5],
            [None, 1, None, 100, 100, None, 20]
        ]

    def case(self, i):
        output = []
        for callable_, arg in zip(self.input[i][0], self.input[i][1]):
            if callable_ == 'SubrectangleQueries':
                subrectangleQueries = SubrectangleQueries(*arg)
                output.append(None)
            else:
                output.append(
                    getattr(subrectangleQueries, callable_)(*arg))
        self.assertEqual(output, self.expected[i])

    def test_subrectangleQueries(self):
        for i, _ in enumerate(self.input):
            self.case(i)
