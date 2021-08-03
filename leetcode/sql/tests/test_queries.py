"""
Contains tests to problems.

595. Big Countries
627. Swap Salary
1179. Reformat Department Table
"""

# Authors: Kin-Yip Chien

import json
# import sys
# sys.path.append('..')
import unittest

import pandas as pd
from pandas.testing import assert_frame_equal
from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())


class TestSolution(unittest.TestCase):

    def test_bigCountries(self):
        """
        595. Big Countries
        """
        with open('tables/world.json') as f:
            table = json.loads(f.read())
        world = pd.DataFrame(table['rows']['World'],
                             columns=table['headers']['World'])

        with open('595-big-countries.sql') as f:
            q = f.read()

        result = json.loads('''
        {"headers": ["name", "population", "area"],
         "values": [["Afghanistan", 25500100, 652230],
                    ["Algeria", 37100000, 2381741]]}
        ''')
        
        result_df = pd.DataFrame(result['values'],
                                 columns=result['headers'])
        assert_frame_equal(pysqldf(q), result_df)


if __name__ == '__main__'
    unittest.main()
