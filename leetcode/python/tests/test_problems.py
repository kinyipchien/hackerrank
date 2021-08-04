# TODO: Move classes to separate modules.
"""
Contains tests for LeetCode problems.

485. Max Consecutive Ones
771. Jewels and Stones
977. Squares of a Sorted Array
1089. Duplicate Zeros
1108. Defanging an IP Address
1295. Find Numbers with Even Number of Digits
1431. Kids With the Greatest Number of Candies
1470. Shuffle the Array
1476. Subrectangle Queries
1480. Running Sum of 1d Array
1512. Number of Good Pairs
1603. Design Parking System
1672. Richest Customer Wealth
1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
1920. Build Array from Permutation
1929. Concatenation of Array
"""

# Authors: Kin-Yip Chien

import sys
sys.path.append('..')
import unittest

from problems import ParkingSystem, Solution, SubrectangleQueries


class TestParkingSystem(unittest.TestCase):
    """
    1603. Design Parking System
    """

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


class TestSolution(unittest.TestCase):

    def test_buildArray(self):
        """
        1920. Build Array from Permutation
        """
        s = Solution()

        nums = [0, 2, 1, 5, 3, 4]
        self.assertEqual(s.buildArray(nums), [0, 1, 2, 4, 5, 3])

        nums = [5, 0, 1, 2, 3, 4]
        self.assertEqual(s.buildArray(nums), [4, 5, 0, 1, 2, 3])

    def test_defangIPaddr(self):
        """
        1108. Defanging an IP Address
        """
        s = Solution()

        address = "1.1.1.1"
        self.assertEqual(s.defangIPaddr(address), "1[.]1[.]1[.]1")

        address = "255.100.50.0"
        self.assertEqual(s.defangIPaddr(address), "255[.]100[.]50[.]0")

    def test_duplicateZeros(self):
        """
        1089. Duplicate Zeros
        """
        s = Solution()

        arr = [1, 0, 2, 3, 0, 4, 5, 0]
        s.duplicateZeros(arr)
        self.assertEqual(arr, [1, 0, 0, 2, 3, 0, 0, 4])

        arr = [1, 2, 3]
        s.duplicateZeros(arr)
        self.assertEqual(arr, [1, 2, 3])

    def test_findMaxConsecutiveOnes(self):
        """
        485. Max Consecutive Ones
        """
        s = Solution()

        nums = [1, 1, 0, 1, 1, 1]
        self.assertEqual(s.findMaxConsecutiveOnes(nums), 3)

        nums = [1, 0, 1, 1, 0, 1]
        self.assertEqual(s.findMaxConsecutiveOnes(nums), 2)

    def test_findNumbers(self):
        """
        1295. Find Numbers with Even Number of Digits
        """
        s = Solution()

        nums = [12, 345, 2, 6, 7896]
        self.assertEqual(s.findNumbers(nums), 2)

        nums = [555, 901, 482, 1771]
        self.assertEqual(s.findNumbers(nums), 1)

        nums = [999999999999999]
        self.assertEqual(s.findNumbers(nums), 0)

        nums = [100000]
        self.assertEqual(s.findNumbers(nums), 1)

    def test_getConcatenation(self):
        """
        1929. Concatenation of Array
        """
        s = Solution()

        nums = [1, 2, 1]
        self.assertEqual(s.getConcatenation(nums), [1, 2, 1, 1, 2, 1])

        nums = [1, 3, 2, 1]
        self.assertEqual(
            s.getConcatenation(nums), [1, 3, 2, 1, 1, 3, 2, 1])

    def test_kidsWithCandies(self):
        """
        1431. Kids With the Greatest Number of Candies
        """
        s = Solution()

        candies = [2, 3, 5, 1, 3]
        extraCandies = 3
        self.assertEqual(s.kidsWithCandies(candies, extraCandies),
                         [True, True, True, False, True])

        candies = [4, 2, 1, 1, 2]
        extraCandies = 1
        self.assertEqual(s.kidsWithCandies(candies, extraCandies),
                         [True, False, False, False, False])

        candies = [12, 1, 12]
        extraCandies = 10
        self.assertEqual(s.kidsWithCandies(candies, extraCandies),
                         [True, False, True])

    def test_maximumWealth(self):
        """
        1672. Richest Customer Wealth
        """
        s = Solution()

        accounts = [[1, 2, 3], [3, 2, 1]]
        self.assertEqual(s.maximumWealth(accounts), 6)

        accounts = [[1, 5], [7, 3], [3, 5]]
        self.assertEqual(s.maximumWealth(accounts), 10)

        accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
        self.assertEqual(s.maximumWealth(accounts), 17)

    def test_minPartitions(self):
        """
        1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
        """
        s = Solution()

        n = "32"
        self.assertEqual(s.minPartitions(n), 3)

        n = "82734"
        self.assertEqual(s.minPartitions(n), 8)

        n = "27346209830709182346"
        self.assertEqual(s.minPartitions(n), 9)

    def test_numIdenticalPairs(self):
        """
        1512. Number of Good Pairs
        """
        s = Solution()

        nums = [1, 2, 3, 1, 1, 3]
        self.assertEqual(s.numIdenticalPairs(nums), 4)

        nums = [1, 1, 1, 1]
        self.assertEqual(s.numIdenticalPairs(nums), 6)

        nums = [1, 2, 3]
        self.assertEqual(s.numIdenticalPairs(nums), 0)

    def test_numJewelsInStones(self):
        """
        771. Jewels and Stones
        """
        s = Solution()
        jewels = "aA"
        stones = "aAAbbbb"
        self.assertEqual(s.numJewelsInStones(jewels, stones), 3)

        jewels = "z"
        stones = "ZZ"
        self.assertEqual(s.numJewelsInStones(jewels, stones), 0)

    def test_runningSum(self):
        """
        1480. Running Sum of 1d Array
        """
        s = Solution()

        nums = [1, 2, 3, 4]
        self.assertEqual(s.runningSum(nums), [1, 3, 6, 10])

        nums = [1, 1, 1, 1, 1]
        self.assertEqual(s.runningSum(nums), [1, 2, 3, 4, 5])

        nums = [3, 1, 2, 10, 1]
        self.assertEqual(s.runningSum(nums), [3, 4, 6, 16, 17])

    def test_shuffle(self):
        """
        1470. Shuffle the Array
        """
        s = Solution()

        nums = [2, 5, 1, 3, 4, 7]
        n = 3
        self.assertEqual(s.shuffle(nums, n), [2, 3, 5, 4, 1, 7])

        nums = [1, 2, 3, 4, 4, 3, 2, 1]
        n = 4
        self.assertEqual(s.shuffle(nums, n), [1, 4, 2, 3, 3, 2, 4, 1])

        nums = [1, 1, 2, 2]
        n = 2
        self.assertEqual(s.shuffle(nums, n), [1, 2, 1, 2])

    def test_sortedSquares(self):
        """
        977. Squares of a Sorted Array
        """
        s = Solution()

        nums = [-4, -1, 0, 3, 10]
        self.assertEqual(s.sortedSquares(nums), [0, 1, 9, 16, 100])

        nums = [-7, -3, 2, 3, 11]
        self.assertEqual(s.sortedSquares(nums), [4, 9, 9, 49, 121])


class TestSubrectangleQueries(unittest.TestCase):
    """
    1476. Subrectangle Queries
    """

    def setUp(self):
        self.input = [
            [
                ["SubrectangleQueries",
                 "getValue",
                 "updateSubrectangle",
                 "getValue",
                 "getValue",
                 "updateSubrectangle",
                 "getValue",
                 "getValue"],
                [[[[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]]],
                 [0, 2],
                 [0, 0, 3, 2, 5],
                 [0, 2],
                 [3, 1],
                 [3, 0, 3, 2, 10],
                 [3, 1],
                 [0, 2]]
            ],
            [
                ["SubrectangleQueries",
                 "getValue",
                 "updateSubrectangle",
                 "getValue",
                 "getValue",
                 "updateSubrectangle",
                 "getValue"],
                [[[[1, 1, 1], [2, 2, 2], [3, 3, 3]]],
                 [0, 0],
                 [0, 0, 2, 2, 100],
                 [0, 0],
                 [2, 2],
                 [1, 1, 2, 2, 20],
                 [2, 2]]
            ]
        ]
        self.expected = [
            [None, 1, None, 5, 5, None, 10, 5],
            [None, 1, None, 100, 100, None, 20]
        ]

    def case(self, i):
        output = []
        for callable_, arg in zip(self.input[i][0], self.input[i][1]):
            if callable_ == 'SubrectangleQueries':
                subrectangleQueries = SubrectangleQueries(*arg)
                output.append(None)
            else:
                output.append(
                    getattr(subrectangleQueries, callable_)(*arg))
        self.assertEqual(output, self.expected[i])

    def test_subrectangleQueries(self):
        for i in range(len(self.input)):
            self.case(i)


if __name__ == '__main__':
    unittest.main()
