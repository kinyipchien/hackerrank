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
1512. Number of Good Pairs
"""
from typing import List


class Solution:

    def numIdenticalPairs(self, nums: List[int]) -> int:
        """
        Return the number of *good* pairs given an array of integers.

        A pair `(i,j)` is called *good* if `nums[i]` == `nums[j]` and
        `i` < `j`.

        Parameters
        ----------
        nums : list of int
            Array of integers.

        Returns
        -------
        pairs : int
            Number of good pairs.

        Examples
        --------
        >>> soln = Solution()
        >>> nums = [1, 2, 3, 1, 1, 3]
        >>> soln.numIdenticalPairs(nums)
        4

        >>> soln = Solution()
        >>> nums = [1, 1, 1, 1]
        >>> soln.numIdenticalPairs(nums)
        6

        >>> soln = Solution()
        >>> nums = [1, 2, 3]
        >>> soln.numIdenticalPairs(nums)
        0

        Notes
        -----
        * `1 <= nums.length <= 100`
        * `1 <= nums[i] <= 100`
        """
        # O(n) Time. O(n) Space.
        c = {}
        pairs = 0
        for num in nums:
            if num in c:
                pairs += c[num]
                c[num] += 1
            else:
                c[num] = 1
        return pairs


if __name__ == '__main__':
    import doctest
    doctest.testmod()
