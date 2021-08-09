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
1431. Kids With the Greatest Number of Candies
"""
from typing import List


class Solution:

    def kidsWithCandies(
        self, candies: List[int], extraCandies: int
    ) -> List[bool]:
        """
        Returns a boolean array denoting whether each of n kids has the
        greatest number of candies.

        A kid has the greatest number of candies if they have the most
        candies among the kids after receiving all the extraCandies.

        Note that multiple kids can have the greatest number of
        candies.

        Parameters
        ----------
        candies : list of int
            An integer array, where each `candies[i]` represents the
            number of candies the `ith` kid has.
        extraCandies : int
            Number of extra candies that you have.

        Returns
        -------
        list of bool
            Whether each kid has the greatest number of candies.
            `result[i]` is `true` if, after giving the `ith` kid all
            the `extraCandies`, they will have the **greatest number**
            of candies among all the kids, or `false` otherwise*

        Examples
        --------
        >>> soln = Solution()
        >>> candies = [2, 3, 5, 1, 3]
        >>> extraCandies = 3
        >>> soln.kidsWithCandies(candies, extraCandies)
        [True, True, True, False, True]

        >>> soln = Solution()
        >>> candies = [4, 2, 1, 1, 2]
        >>> extraCandies = 1
        >>> soln.kidsWithCandies(candies, extraCandies)
        [True, False, False, False, False]

        >>> soln = Solution()
        >>> candies = [12, 1, 12]
        >>> extraCandies = 10
        >>> soln.kidsWithCandies(candies, extraCandies)
        [True, False, True]

        Notes
        -----
        * `n == candies.length`
        * `2 <= n <= 100`
        * `1 <= candies[i] <= 100`
        * `1 <= extraCandies <= 50`
        """
        # O(n) Time, O(n) Space.
        threshold = max(candies) - extraCandies
        return [kid >= threshold for kid in candies]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
