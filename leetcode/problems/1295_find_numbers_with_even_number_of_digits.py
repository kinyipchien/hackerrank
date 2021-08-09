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
1295. Find Numbers with Even Number of Digits
"""
from typing import List


class Solution:

    def _has_even_num_digits(self, num:int) -> bool:
        """
        Checks if a number has an even number of digits.

        Helper method for findNumbers().

        Parameters
        ----------
        x : int
            Number to check.

        Returns
        -------
        even_num_digits : bool
            Whether number has an even number of digits.
        """
        even_num_digits = False
        while num >= 10:
            even_num_digits = not even_num_digits
            num //= 10
        return even_num_digits

    def findNumbers(self, nums: List[int]) -> int:
        """
        Returns how many numbers in an input array contain an **even
        number** of digits.

        Parameters
        ----------
        nums : list of int
            Array of integers.

        Returns
        -------
        int
            Count of integers containing an even number of digits.

        Examples
        --------
        >>> soln = Solution()
        >>> nums = [12, 345, 2, 6, 7896]
        >>> soln.findNumbers(nums)
        2

        >>> soln = Solution()
        >>> nums = [555, 901, 482, 1771]
        >>> soln.findNumbers(nums)
        1

        >>> soln = Solution()
        >>> nums = [999999999999999]
        >>> soln.findNumbers(nums)
        0

        >>> soln = Solution()
        >>> nums = [100000]
        >>> soln.findNumbers(nums)
        1

        Notes
        -----
        * `1 <= nums.length <= 500`
        * `1 <= nums[i] <= 10^5`
        """
        # O(nlogn) Time, O(1) Space.
        return sum(self._has_even_num_digits(num) for num in nums)

        # BUG: math.log10 is inaccurate for 1e(x) +/- 1 when x > 14.
#         count_even_num_digits = 0
#         for num in nums:
#             digits = floor(log10(num)) + 1
#             if digits % 2 == 0:
#                 count_even_num_digits += 1
#         return count_even_num_digits


if __name__ == '__main__':
    import doctest
    doctest.testmod()
