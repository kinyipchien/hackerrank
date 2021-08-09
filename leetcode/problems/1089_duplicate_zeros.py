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
1089. Duplicate Zeros
"""
from typing import List


class Solution:

    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Duplicates each occurrence of zero in an input array in-place,
        shifting the remaining elements to the right.

        Elements beyond the length of the original array are
        not written.

        Parameters
        ----------
        arr : list of int
            Array of integers.

        Returns
        -------
        None

        Examples
        --------
        >>> soln = Solution()
        >>> arr = [1, 0, 2, 3, 0, 4, 5, 0]
        >>> soln.duplicateZeros(arr)
        >>> arr
        [1, 0, 0, 2, 3, 0, 0, 4]

        >>> soln = Solution()
        >>> arr = [1, 2, 3]
        >>> soln.duplicateZeros(arr)
        >>> arr
        [1, 2, 3]

        Notes
        -----
        * `1 <= arr.length <= 10000`
        * `0 <= arr[i] <= 9`
        """
        # O(n) Time, O(1) Space.
        zeros = arr.count(0)
        n = len(arr)
        for i in range(n - 1, -1, -1):
            if zeros == 0:
                break
            if i + zeros < n:
                arr[i + zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < n:
                    arr[i + zeros] = arr[i]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
