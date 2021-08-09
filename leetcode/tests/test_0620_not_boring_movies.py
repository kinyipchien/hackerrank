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
620. Not Boring Movies
"""
import json
import unittest

import pandas as pd
from pandas.testing import assert_frame_equal
from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())

table = json.loads('''
    {"headers": {"cinema": ["id", "movie", "description", "rating"]},
     "rows": {"cinema": [[1, "War", "great 3D", 8.9],
                         [2, "Science", "fiction", 8.5],
                         [3, "irish", "boring", 6.2],
                         [4, "Ice song", "Fantacy", 8.6],
                         [5, "House card", "Interesting", 9.1]]}}
    ''')
cinema = pd.DataFrame(table['rows']['cinema'],
                      columns=table['headers']['cinema'])


class TestSolution(unittest.TestCase):

    def test_not_boring_movies(self):
        with open('src/problems/0620-not-boring-movies.sql') as f:
            q = f.read()

        result = json.loads('''
        {"headers": ["id", "movie", "description", "rating"],
         "values": [[5, "House card", "Interesting", 9.1],
                    [1, "War", "great 3D", 8.9]]}
        ''')

        result_df = pd.DataFrame(result['values'],
                                 columns=result['headers'])
        assert_frame_equal(pysqldf(q), result_df)
