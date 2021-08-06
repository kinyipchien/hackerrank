"""
Contains tests to problems.

175. Combine Two Tables
595. Big Countries
620. Not Boring Movies
627. Swap Salary
1179. Reformat Department Table
"""

# Authors: Kin-Yip Chien

import json
import unittest

import pandas as pd
from pandas.testing import assert_frame_equal
from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())


with open('../tables/person-address.json') as f:
    table = json.loads(f.read())
address = pd.DataFrame(table['rows']['Address'],
                      columns=table['headers']['Address'])

with open('../tables/cinema.json') as f:
    table = json.loads(f.read())
cinema = pd.DataFrame(table['rows']['cinema'],
                      columns=table['headers']['cinema'])

with open('../tables/department.json') as f:
    table = json.loads(f.read())
department = pd.DataFrame(table['rows']['Department'],
                          columns=table['headers']['Department'])

with open('../tables/person-address.json') as f:
    table = json.loads(f.read())
person = pd.DataFrame(table['rows']['Person'],
                      columns=table['headers']['Person'])

#     BUG: pandasql doesn't support DELETE or UPDATE clauses.
# with open('../tables/salary.json') as f:
#     table = json.loads(f.read())
# salary = pd.DataFrame(table['rows']['salary'],
#                      columns=table['headers']['salary'])

with open('../tables/world.json') as f:
    table = json.loads(f.read())
world = pd.DataFrame(table['rows']['World'],
                     columns=table['headers']['World'])


class TestSolution(unittest.TestCase):

    def test_bigCountries(self):
        """
        595. Big Countries
        """
        with open('../595-big-countries.sql') as f:
            q = f.read()

        result = json.loads('''
        {"headers": ["name", "population", "area"],
         "values": [["Afghanistan", 25500100, 652230],
                    ["Algeria", 37100000, 2381741]]}
        ''')

        result_df = pd.DataFrame(result['values'],
                                 columns=result['headers'])
        assert_frame_equal(pysqldf(q), result_df)

    def test_combine_two_tables(self):
        """
        175. Combine Two Tables
        """
        with open('../175-combine-two-tables.sql') as f:
            q = f.read()

        result = json.loads('''
        {"headers": ["FirstName", "LastName", "City", "State"],
         "values": [["Allen", "Wang", null, null]]}
        ''')

        result_df = pd.DataFrame(result['values'],
                                 columns=result['headers'])
        assert_frame_equal(pysqldf(q), result_df)

    def test_not_boring_movies(self):
        """
        620. Not Boring Movies
        """
        with open('../620-not-boring-movies.sql') as f:
            q = f.read()

        result = json.loads('''
        {"headers": ["id", "movie", "description", "rating"],
         "values": [[5, "House card", "Interesting", 9.1],
                    [1, "War", "great 3D", 8.9]]}
        ''')

        result_df = pd.DataFrame(result['values'],
                                 columns=result['headers'])
        assert_frame_equal(pysqldf(q), result_df)

    def test_reformat_department_table(self):
        """
        1179. Reformat Department Table
        """
        with open('../1179-reformat-department-table.sql') as f:
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

#     BUG: pandasql doesn't support DELETE or UPDATE clauses.
#     def test_swapSalary(self):
#         """
#         627. Swap Salary
#         """
#         with open('../627-swap-salary.sql') as f:
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


if __name__ == '__main__':
    unittest.main()
