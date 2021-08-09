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
1672. Richest Customer Wealth
"""
from typing import List


class Solution:

    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """
        Returns *the **wealth** that the richest customer has*.

        A customer's **wealth** is the amount of money they have in all
        their bank accounts. The richest customer is the customer that
        has the maximum **wealth**.

        Parameters
        ----------
        accounts : list of list of int
            `m x n` integer grid where `accounts[i][j]` is the amount
            of money the `ith` customer has in the `jth` bank.

        Returns
        -------
        int
            Wealth of the richest customer.

        Examples
        --------
        >>> soln = Solution()
        >>> accounts = [[1, 2, 3], [3, 2, 1]]
        >>> soln.maximumWealth(accounts)
        6

        >>> soln = Solution()
        >>> accounts = [[1, 5], [7, 3], [3, 5]]
        >>> soln.maximumWealth(accounts)
        10

        >>> soln = Solution()
        >>> accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
        >>> soln.maximumWealth(accounts)
        17

        Notes
        -----
        * `m == accounts.length`
        * `n == accounts[i].length`
        * `1 <= m, n <= 50`
        * `1 <= accounts[i][j] <= 100`
        """
        # O(m*n) Time, O(1) Space.
        return max(map(sum, accounts))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
