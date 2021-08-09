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
771. Jewels and Stones
"""


class Solution:

    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """
        Computes how many of the stones you have are also jewels.

        Parameters
        ----------
        jewels : str
            String representing the types of stones that are jewels.
            Letters are case sensitive.
        stones : str
            String representing the stones you have. Letters are case
            sensitive.

        Returns
        -------
        int
            Number of jewels you have.

        Examples
        --------
        >>> soln = Solution()
        >>> jewels = "aA"
        >>> stones = "aAAbbbb"
        >>> soln.numJewelsInStones(jewels, stones)
        3

        >>> soln = Solution()
        >>> jewels = "z"
        >>> stones = "ZZ"
        >>> soln.numJewelsInStones(jewels, stones)
        0

        Notes
        -----
        * `1 <= jewels.length, stones.length <= 50`
        * `jewels` and `stones` consist of only English letters.
        * All the characters of `jewels` are **unique**.
        """
        # O(j + s) Time, O(j) Space.
        set_jewels = set(jewels)
        return sum(stone in set_jewels for stone in stones)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
