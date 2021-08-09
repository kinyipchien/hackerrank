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
1603. Design Parking System
"""


class ParkingSystem:
    """
    A parking system for a parking lot.

    The parking lot has three kinds of parking spaces: big, medium, and
    small, with a fixed number of slots for each size.

    Parameters
    ----------
    big : int
        Number of big slots.
    medium : int
        Number of medium slots.
    small : int
        Number of small slots.

    Attributes
    ----------
    spaces : dict
        Number of slots for each size.

    Examples
    --------
    >>> parking_system = ParkingSystem(1, 1, 0)
    >>> parking_system.addCar(1)
    True
    >>> parking_system.addCar(2)
    True
    >>> parking_system.addCar(3)
    False
    >>> parking_system.addCar(1)
    False

    Notes
    -----
    * `0 <= big, medium, small <= 1000`
    * `carType` is `1`, `2`, or `3`
    * At most `1000` calls will be made to `addCar`
    """

    def __init__(self, big: int, medium: int, small: int):
        self.spaces = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        """
        Checks whether there is a parking space of `carType` for the
        car that wants to get into the parking lot.

        **A car can only park in a parking space of its `carType`**. If
        there is no space available, return `false`, else park the car
        in that size space and return `true`.

        Parameters
        ----------
        carType : int
            Kind of car type.
            - 1 : big
            - 2 : medium
            - 3 : small

        Returns
        -------
        bool
            Whether there is a space available.
        """
        # O(1) Time, O(1) Space.
        if self.spaces[carType]:
            self.spaces[carType] -= 1
            return True
        return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()
