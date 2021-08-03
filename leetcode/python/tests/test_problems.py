"""
Contains tests to problems.

485. Max Consecutive Ones
977. Squares of a Sorted Array
1089. Duplicate Zeros
1108. Defanging an IP Address
1295. Find Numbers with Even Number of Digits
1431. Kids With the Greatest Number of Candies
1470. Shuffle the Array
1480. Running Sum of 1d Array
1672. Richest Customer Wealth
1920. Build Array from Permutation
1929. Concatenation of Array
"""

# Authors: Kin-Yip Chien

import sys
sys.path.append('..')
import unittest

from problems import Solution


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
        # TODOC: Problem number.
        s = Solution()

        arr = [1, 0, 2, 3, 0, 4, 5, 0]
        s.duplicateZeros(arr)
        self.assertEqual(arr, [1, 0, 0, 2, 3, 0, 0, 4])

        arr = [1, 2, 3]
        s.duplicateZeros(arr)
        self.assertEqual(arr, [1, 2, 3])

    def test_findMaxConsecutiveOnes(self):
        # TODOC: Problem number.
        s = Solution()

        nums = [1, 1, 0, 1, 1, 1]
        self.assertEqual(s.findMaxConsecutiveOnes(nums), 3)

        nums = [1, 0, 1, 1, 0, 1]
        self.assertEqual(s.findMaxConsecutiveOnes(nums), 2)

    def test_findNumbers(self):
        # TODOC: Problem number.
        s = Solution()

        nums = [12, 345, 2, 6, 7896]
        self.assertEqual(s.findNumbers(nums), 2)

        nums = [555, 901, 482, 1771]
        self.assertEqual(s.findNumbers(nums), 1)

        nums = [999999999999999]
        self.assertEqual(s.findNumbers(nums), 0)

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
        # TODOC: Problem number.
        s = Solution()

        nums = [-4, -1, 0, 3, 10]
        self.assertEqual(s.sortedSquares(nums), [0, 1, 9, 16, 100])

        nums = [-7, -3, 2, 3, 11]
        self.assertEqual(s.sortedSquares(nums), [4, 9, 9, 49, 121])


if __name__ == '__main__':
    unittest.main()
