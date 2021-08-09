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
1720. Decode XORed Array
"""
from typing import List


class Solution:

    def decode(self, encoded: List[int], first: int) -> List[int]:
        """
        Decodes an encoded array.

        An integer array that consists of `n` non-negative integers is
        encoded into another integer array of length `n - 1`, such that
        `encoded[i] = arr[i] XOR arr[i + 1]`. For example, if
        `arr = [1,0,2,1]`, then `encoded = [1,2,3]`.

        Parameters
        ----------
        encoded : list of int
            Encoded array.
        first : int
            First element of decoded array.

        Returns
        -------
        decoded : list of int
            Decoded array.

        Examples
        --------
        >>> soln = Solution()
        >>> encoded = [1, 2, 3]
        >>> first = 1
        >>> soln.decode(encoded, first)
        [1, 0, 2, 1]

        >>> soln = Solution()
        >>> encoded = [6, 2, 7, 3]
        >>> first = 4
        >>> soln.decode(encoded, first)
        [4, 2, 0, 7, 4]

        Notes
        -----
        * `2 <= n <= 10^4`
        * `encoded.length == n - 1`
        * `0 <= encoded[i] <= 10^5`
        * `0 <= first <= 10^5`
        """
        # O(n) Time, O(n) Space.
        decoded = [first]
        for elem in encoded:
            decoded.append(decoded[-1] ^ elem)
        return decoded


if __name__ == '__main__':
    import doctest
    doctest.testmod()
