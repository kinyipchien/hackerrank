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
627. Swap Salary
"""
import json
import unittest

import pandas as pd
from pandas.testing import assert_frame_equal
from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())

table = json.loads('''
    {"headers": {"salary": ["id", "name", "sex", "salary"]},
     "rows": {"salary": [[1, "A", "m", 2500],
                         [2, "B" ,"f" ,1500],
                         [3, "C" ,"m" ,5500],
                         [4, "D" ,"f" ,500]]}}
    ''')
salary = pd.DataFrame(table['rows']['salary'],
                      columns=table['headers']['salary'])


# class TestSolution(unittest.TestCase):

#     BUG: pandasql doesn't support DELETE or UPDATE clauses.
#     def test_swap_salary(self):
#         with open('src/problems/0627-swap-salary.sql') as f:
#             q = f.read()

#         result = json.loads('''
#         {"headers": ["id", "name", "sex", "salary"],
#          "values": [[1, "A", "f", 2500],
#                     [2, "B", "m", 1500],
#                     [3, "C", "f", 5500],
#                     [4, "D", "m", 500]]}
#         ''')

#         result_df = pd.DataFrame(result['values'],
#                                  columns=result['headers'])
#         assert_frame_equal(pysqldf(q), result_df)
