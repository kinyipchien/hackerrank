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
from importlib import import_module
ParkingSystem = (
    import_module(
        'problems.1603_design_parking_system')
    .ParkingSystem)
import unittest


class TestParkingSystem(unittest.TestCase):

    def setUp(self):
        self.input = [
            ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"],
            [[1, 1, 0], [1], [2], [3], [1]]]
        self.expected = [None, True, True, False, False]

    def test_ParkingSystem(self):
        output = []
        for callable_, arg in zip(self.input[0], self.input[1]):
            if callable_ == 'ParkingSystem':
                parkingSystem = ParkingSystem(*arg)
                output.append(None)
            else:
                output.append(
                    getattr(parkingSystem, callable_)(*arg))
        self.assertEqual(output, self.expected)
