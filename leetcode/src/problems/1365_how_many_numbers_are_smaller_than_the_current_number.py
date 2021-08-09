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
1365. How Many Numbers Are Smaller Than the Current Number
"""
from typing import List


class Solution:

    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """
        For a given array `nums`, returns an array where `array[i]` is
        how many numbers in the array are smaller than `nums[i]`.

        Parameters
        ----------
        nums : list of int
            Integer array.

        Returns
        -------
        list of int
            Result array.

        Examples
        --------
        >>> soln = Solution()
        >>> nums = [8, 1, 2, 2, 3]
        >>> soln.smallerNumbersThanCurrent(nums)
        [4, 0, 1, 1, 3]

        >>> soln = Solution()
        >>> nums = [6, 5, 4, 8]
        >>> soln.smallerNumbersThanCurrent(nums)
        [2, 1, 0, 3]

        >>> soln = Solution()
        >>> nums = [7,7,7,7]
        >>> soln.smallerNumbersThanCurrent(nums)
        [0, 0, 0, 0]

        Notes
        -----
        * `2 <= nums.length <= 500`
        * `0 <= nums[i] <= 100`
        """
        # O(n) Time, O(n) Space.
        count = [0] * (max(nums) + 2)
        for num in nums:
            count[num + 1] += 1
        for i, _ in enumerate(count[1:], 1):
            count[i] += count[i - 1]
        return [count[num] for num in nums]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
