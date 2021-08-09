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
1470. Shuffle the Array
"""
from typing import List


class Solution:

    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """
        Given an array in the form `[x1,x2,...,xn,y1,y2,...,yn]`,
        returns an array in the form `[x1,y1,x2,y2,...,xn,yn]`.

        Parameters
        ----------
        nums : list of int
            Integer array consisting of `2n` elements in the form
            `[x1,x2,...,xn,y1,y2,...,yn]`.
        n : int
            Positive integer.

        Returns
        -------
        shuffled : list of int
            Shuffled array in the form `[x1,y1,x2,y2,...,xn,yn]`.

        Examples
        --------
        >>> soln = Solution()
        >>> nums = [2, 5, 1, 3, 4, 7]
        >>> n = 3
        >>> soln.shuffle(nums, n)
        [2, 3, 5, 4, 1, 7]

        >>> soln = Solution()
        >>> nums = [1, 2, 3, 4, 4, 3, 2, 1]
        >>> n = 4
        >>> soln.shuffle(nums, n)
        [1, 4, 2, 3, 3, 2, 4, 1]

        >>> soln = Solution()
        >>> nums = [1, 1, 2, 2]
        >>> n = 2
        >>> soln.shuffle(nums, n)
        [1, 2, 1, 2]

        Notes
        -----
        * `1 <= n <= 500`
        * `nums.length == 2n`
        * `1 <= nums[i] <= 10^3`
        """
        # O(n) Time, O(n) Space.
        shuffled = [None] * 2*n
        shuffled[::2], shuffled[1::2] = nums[:n], nums[n:]
        return shuffled


if __name__ == '__main__':
    import doctest
    doctest.testmod()
