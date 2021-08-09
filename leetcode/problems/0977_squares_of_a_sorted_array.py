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
977. Squares of a Sorted Array
"""
from typing import List


class Solution:

    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Returns an array of the squares of each number in an input
        array, sorted in non-decreasing order.

        Parameters
        ----------
        nums : list of int
            Integer array sorted in non-decreasing order.

        Returns
        -------
        sorted_squares : list of int
            The squares of the input numbers sorted in non-decreasing
            order.

        Examples
        --------
        >>> soln = Solution()
        >>> nums = [-4, -1, 0, 3, 10]
        >>> soln.sortedSquares(nums)
        [0, 1, 9, 16, 100]

        >>> soln = Solution()
        >>> nums = [-7, -3, 2, 3, 11]
        >>> soln.sortedSquares(nums)
        [4, 9, 9, 49, 121]

        Notes
        -----
        * `1 <= nums.length <= 10^4`
        * `-10^4 <= nums[i] <= 10^4`
        * `nums` is sorted in **non-decreasing** order.
        """
        # O(n) Time, O(n) Space.
        n = len(nums)
        sorted_squares = [None] * n
        left, right = 0, n - 1
        for i in range(n - 1, -1, -1):
            left_squared = nums[left] ** 2
            right_squared = nums[right] ** 2
            if left_squared >= right_squared:
                sorted_squares[i] = left_squared
                left += 1
            else:
                sorted_squares[i] = right_squared
                right -= 1
        return sorted_squares


if __name__ == '__main__':
    import doctest
    doctest.testmod()
