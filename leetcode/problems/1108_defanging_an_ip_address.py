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
1108. Defanging an IP Address
"""
from typing import List


class Solution:

    def defangIPaddr(self, address: str) -> str:
        """
        Defangs a (IPv4) IP `address` by replacing every period `"."`
        with `"[.]"`.

        Parameters
        ----------
        address : str
            IPv4 address.

        Returns
        -------
        str
            Defanged IPv4 address.

        Examples
        --------
        >>> soln = Solution()
        >>> address = "1.1.1.1"
        >>> soln.defangIPaddr(address)
        '1[.]1[.]1[.]1'

        >>> soln = Solution()
        >>> address = "255.100.50.0"
        >>> soln.defangIPaddr(address)
        '255[.]100[.]50[.]0'
        """
        # O(n * (m1 + m2/m1)) Time, O(n) Space.
        # n : length of the string
        # m1 : length of the searched for string.
        # m2 : length of the replacement.
        return address.replace('.', '[.]')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
