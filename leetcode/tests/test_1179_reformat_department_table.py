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
1179. Reformat Department Table
"""
import json
import unittest

import pandas as pd
from pandas.testing import assert_frame_equal
from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())

table = json.loads('''
    {"headers": {"Department": ["id", "revenue", "month"]},
     "rows": {"Department": [[1 ,8000, "Jan"],
                             [2 ,9000, "Jan"],
                             [3 ,10000, "Feb"],
                             [1 ,7000, "Feb"],
                             [1 ,6000, "Mar"]]}}
    ''')
department = pd.DataFrame(table['rows']['Department'],
                      columns=table['headers']['Department'])


class TestSolution(unittest.TestCase):

    def test_reformat_department_table(self):
        with open('src/problems/1179-reformat-department-table.sql') as f:
            q = f.read()

        result = json.loads('''
        {"headers": ["id", "Jan_Revenue", "Feb_Revenue", "Mar_Revenue",
                     "Apr_Revenue", "May_Revenue", "Jun_Revenue",
                     "Jul_Revenue", "Aug_Revenue", "Sep_Revenue",
                     "Oct_Revenue", "Nov_Revenue", "Dec_Revenue"],
         "values":
             [[1, 8000, 7000, 6000, null, null, null,
               null, null, null, null, null, null],
              [2, 9000, null, null, null, null, null,
               null, null, null, null, null, null],
              [3, null, 10000, null, null, null, null,
               null, null, null, null, null, null]]}
        ''')

        result_df = pd.DataFrame(result['values'],
                                 columns=result['headers'])
        assert_frame_equal(pysqldf(q), result_df)
