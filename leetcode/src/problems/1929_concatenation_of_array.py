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
1929. Concatenation of Array
"""
from typing import List


class Solution:

    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        Returns the concatenation of an array with itself.

        Parameters
        ----------
        nums : list of int
            Integer array.

        Returns
        -------
        ans : list of int
            Concatenated array.

        Examples
        --------
        >>> soln = Solution()
        >>> nums = [1, 2, 1]
        >>> soln.getConcatenation(nums)
        [1, 2, 1, 1, 2, 1]

        >>> soln = Solution()
        >>> nums = [1, 3, 2, 1]
        >>> soln.getConcatenation(nums)
        [1, 3, 2, 1, 1, 3, 2, 1]

        Notes
        -----
        1929. Concatenation of Array

        Constraints:
        * `n == nums.length`
        * `1 <= n <= 1000`
        * `1 <= nums[i] <= 1000`
        """
        # O(n) Time, O(n) Space.
        return nums + nums


if __name__ == '__main__':
    import doctest
    doctest.testmod()
