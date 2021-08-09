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
1480. Running Sum of 1d Array
"""
from typing import List


class Solution:

    def runningSum(self, nums: List[int]) -> List[int]:
        """
        Returns the running sum of an array where
        `runningSum[i] = sum(nums[0]…nums[i])`.

        Parameters
        ----------
        nums : list of int
            Array.

        Returns
        -------
        running_sum : list of int
            Running sum.

        Examples
        --------
        >>> soln = Solution()
        >>> nums = [1, 2, 3, 4]
        >>> soln.runningSum(nums)
        [1, 3, 6, 10]

        >>> soln = Solution()
        >>> nums = [1, 1, 1, 1, 1]
        >>> soln.runningSum(nums)
        [1, 2, 3, 4, 5]

        >>> soln = Solution()
        >>> nums = [3, 1, 2, 10, 1]
        >>> soln.runningSum(nums)
        [3, 4, 6, 16, 17]

        Notes
        -----
        * `1 <= nums.length <= 1000`
        * `-10^6 <= nums[i] <= 10^6`
        """
        # O(n) Time, O(n) Space.
        for i, _ in enumerate(nums[1:], 1):
            nums[i] += nums[i - 1]
        return nums


if __name__ == '__main__':
    import doctest
    doctest.testmod()
