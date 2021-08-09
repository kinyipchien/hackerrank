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
182. Duplicate Emails
"""
import json
import unittest

import pandas as pd
from pandas.testing import assert_frame_equal
from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())

table = json.loads('''
    {"headers":
        {"Person": ["Id", "Email"]},
     "rows":
        {"Person": [[1, "a@b.com"], [2, "c@d.com"], [3, "a@b.com"]]}}
    ''')
person = pd.DataFrame(table['rows']['Person'],
                      columns=table['headers']['Person'])


class TestSolution(unittest.TestCase):

    def test_duplicate_emails(self):
        with open('problems/0182-duplicate-emails.sql') as f:
            q = f.read()

        result = json.loads('''
        {"headers": ["Email"], "values": [["a@b.com"]]}
        ''')

        result_df = pd.DataFrame(result['values'],
                                 columns=result['headers'])
        assert_frame_equal(pysqldf(q), result_df)
