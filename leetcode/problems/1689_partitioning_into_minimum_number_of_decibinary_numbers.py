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
1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
"""
from typing import List


class Solution:

    def minPartitions(self, n: str) -> int:
        """
        Returns the **minimum** number of positive **deci-binary**
        numbers needed to sum up to `n`*.

        A decimal number is called **deci-binary** if each of its
        digits is either `0` or `1` without any leading zeros. For
        example, `101` and `1100` are **deci-binary**, while `112` and
        `3001` are not.

        Parameters
        ----------
        n : str
            String representing a positive decimal integer.

        Returns
        -------
        int
            **Minimum** number of positive **deci-binary** numbers
            needed to sum up to `n`*.

        Examples
        --------
        >>> soln = Solution()
        >>> n = "32"
        >>> soln.minPartitions(n)
        3

        >>> soln = Solution()
        >>> n = "82734"
        >>> soln.minPartitions(n)
        8

        >>> soln = Solution()
        >>> n = "27346209830709182346"
        >>> soln.minPartitions(n)
        9

        Notes
        -----
        * `1 <= n.length <= 10^5`
        * `n` consists of only digits.
        * `n` does not contain any leading zeros and represents a
        positive integer.
        """
        # O(n) Time, O(1) Space.
        return int(max(n))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
