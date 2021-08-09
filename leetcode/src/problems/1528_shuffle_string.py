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
1528. Shuffle String
"""
from typing import List


class Solution:

    def restoreString(self, s: str, indices: List[int]) -> str:
        """
        Shuffle a string such that the character at the `ith` position
        moves to the `indices[i]` position.

        Parameters
        ----------
        s : str
            String.
        indices : list of int
            Integer array.

        Returns
        -------
        str
            Shuffled string.

        Examples
        --------
        >>> soln = Solution()
        >>> s = "codeleet"
        >>> indices = [4, 5, 6, 7, 0, 2, 1, 3]
        >>> soln.restoreString(s, indices)
        'leetcode'

        >>> soln = Solution()
        >>> s = "abc"
        >>> indices = [0,1,2]
        >>> soln.restoreString(s, indices)
        'abc'

        >>> soln = Solution()
        >>> s = "aiohn"
        >>> indices = [3, 1, 4, 2, 0]
        >>> soln.restoreString(s, indices)
        'nihao'

        >>> soln = Solution()
        >>> s = "aaiougrt"
        >>> indices = [4, 0, 2, 6, 7, 3, 1, 5]
        >>> soln.restoreString(s, indices)
        'arigatou'

        >>> soln = Solution()
        >>> s = "art"
        >>> indices = [1, 0, 2]
        >>> soln.restoreString(s, indices)
        'rat'

        Notes
        -----
        * `s.length == indices.length == n`
        * `1 <= n <= 100`
        * `s` contains only lower-case English letters.
        * `0 <= indices[i] < n`
        * All values of `indices` are unique (i.e. `indices` is a
        permutation of the integers from `0` to `n - 1`).
        """
        # O(n) Time, O(n) Space.
        restored = [''] * len(s)
        for i, idx in enumerate(indices):
            restored[idx] = s[i]
        return ''.join(restored)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
