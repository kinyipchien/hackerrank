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
595. Big Countries
"""
import json
import unittest

import pandas as pd
from pandas.testing import assert_frame_equal
from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())

table = json.loads('''
    {"headers":
        {"World":
            ["name", "continent", "area", "population", "gdp"]},
     "rows":
        {"World":
            [["Afghanistan", "Asia", 652230, 25500100, 20343000000],
             ["Albania", "Europe", 28748, 2831741, 12960000000],
             ["Algeria", "Africa", 2381741, 37100000, 188681000000],
             ["Andorra", "Europe", 468, 78115, 3712000000],
             ["Angola", "Africa", 1246700, 20609294, 100990000000]]}}
    ''')
world = pd.DataFrame(table['rows']['World'],
                     columns=table['headers']['World'])


class TestSolution(unittest.TestCase):

    def test_big_countries(self):
        with open('src/problems/0595-big-countries.sql') as f:
            q = f.read()

        result = json.loads('''
        {"headers": ["name", "population", "area"],
         "values": [["Afghanistan", 25500100, 652230],
                    ["Algeria", 37100000, 2381741]]}
        ''')

        result_df = pd.DataFrame(result['values'],
                                 columns=result['headers'])
        assert_frame_equal(pysqldf(q), result_df)
