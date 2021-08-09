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
485. Max Consecutive Ones
"""
from typing import List


class Solution:

    def findMaxConsecutiveOnes(self, nums: List[int]) -> List:
        """
        Returns *the maximum number of consecutive `1`'s in the array*.

        Parameters
        ----------
        nums : list of int
            Binary array.

        Returns
        -------
        max_ones : int
            Maximum number of consecutive ones in the array.

        Examples
        --------
        >>> soln = Solution()
        >>> nums = [1, 1, 0, 1, 1, 1]
        >>> soln.findMaxConsecutiveOnes(nums)
        3

        >>> soln = Solution()
        >>> nums = [1, 0, 1, 1, 0, 1]
        >>> soln.findMaxConsecutiveOnes(nums)
        2

        Notes
        -----
        * `1 <= nums.length <= 10^5`
        * `nums[i]` is either `0` or `1`.
        """
        # O(n) Time, O(1) Space.
        ones = max_ones = 0
        for num in nums:
            ones = ones * num + num
            max_ones = max(ones, max_ones)
        return max_ones


if __name__ == '__main__':
    import doctest
    doctest.testmod()
