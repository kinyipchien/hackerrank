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

    def test_buildArray1(self):
        """
        1920. Build Array from Permutation
        """
        nums = [0, 2, 1, 5, 3, 4]
        s = Solution()
        self.assertEqual(s.buildArray(nums), [0, 1, 2, 4, 5, 3])

    def test_buildArray2(self):
        """
        1920. Build Array from Permutation
        """
        nums = [5, 0, 1, 2, 3, 4]
        s = Solution()
        self.assertEqual(s.buildArray(nums), [4, 5, 0, 1, 2, 3])

    def test_defangIPaddr1(self):
        """
        1108. Defanging an IP Address
        """
        address = "1.1.1.1"
        s = Solution()
        self.assertEqual(s.defangIPaddr(address), "1[.]1[.]1[.]1")

    def test_defangIPaddr2(self):
        """
        1108. Defanging an IP Address
        """
        address = "255.100.50.0"
        s = Solution()
        self.assertEqual(s.defangIPaddr(address), "255[.]100[.]50[.]0")

    def test_duplicateZeros1(self):
        # TODOC: Problem number.
        arr = [1, 0, 2, 3, 0, 4, 5, 0]
        s = Solution()
        s.duplicateZeros(arr)
        self.assertEqual(arr, [1, 0, 0, 2, 3, 0, 0, 4])

    def test_duplicateZeros2(self):
        # TODOC: Problem number.
        arr = [1, 2, 3]
        s = Solution()
        s.duplicateZeros(arr)
        self.assertEqual(arr, [1, 2, 3])

    def test_findMaxConsecutiveOnes1(self):
        # TODOC: Problem number.
        nums = [1, 1, 0, 1, 1, 1]
        s = Solution()
        self.assertEqual(s.findMaxConsecutiveOnes(nums), 3)

    def test_findMaxConsecutiveOnes2(self):
        # TODOC: Problem number.
        nums = [1, 0, 1, 1, 0, 1]
        s = Solution()
        self.assertEqual(s.findMaxConsecutiveOnes(nums), 2)

    def test_findNumbers1(self):
        # TODOC: Problem number.
        nums = [12, 345, 2, 6, 7896]
        s = Solution()
        self.assertEqual(s.findNumbers(nums), 2)

    def test_findNumbers2(self):
        # TODOC: Problem number.
        nums = [555, 901, 482, 1771]
        s = Solution()
        self.assertEqual(s.findNumbers(nums), 1)

    def test_findNumbers3(self):
        # TODOC: Problem number.
        nums = [999999999999999]
        s = Solution()
        self.assertEqual(s.findNumbers(nums), 0)

    def test_getConcatenation1(self):
        """
        1929. Concatenation of Array
        """
        nums = [1, 2, 1]
        s = Solution()
        self.assertEqual(s.getConcatenation(nums), [1, 2, 1, 1, 2, 1])

    def test_getConcatenation2(self):
        """
        1929. Concatenation of Array
        """
        nums = [1, 3, 2, 1]
        s = Solution()
        self.assertEqual(
            s.getConcatenation(nums), [1, 3, 2, 1, 1, 3, 2, 1])

    def test_maximumWealth1(self):
        """
        1672. Richest Customer Wealth
        """
        accounts = [[1, 2, 3], [3, 2, 1]]
        s = Solution()
        self.assertEqual(s.maximumWealth(accounts), 6)

    def test_maximumWealth2(self):
        """
        1672. Richest Customer Wealth
        """
        accounts = [[1, 5], [7, 3], [3, 5]]
        s = Solution()
        self.assertEqual(s.maximumWealth(accounts), 10)

    def test_maximumWealth3(self):
        """
        1672. Richest Customer Wealth
        """
        accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
        s = Solution()
        self.assertEqual(s.maximumWealth(accounts), 17)

    def test_runningSum1(self):
        """
        1480. Running Sum of 1d Array
        """
        nums = [1, 2, 3, 4]
        s = Solution()
        self.assertEqual(s.runningSum(nums), [1, 3, 6, 10])

    def test_runningSum2(self):
        """
        1480. Running Sum of 1d Array
        """
        nums = [1, 1, 1, 1, 1]
        s = Solution()
        self.assertEqual(s.runningSum(nums), [1, 2, 3, 4, 5])

    def test_runningSum3(self):
        """
        1480. Running Sum of 1d Array
        """
        nums = [3, 1, 2, 10, 1]
        s = Solution()
        self.assertEqual(s.runningSum(nums), [3, 4, 6, 16, 17])

    def test_shuffle1(self):
        """
        1470. Shuffle the Array
        """
        nums = [2, 5, 1, 3, 4, 7]
        n = 3
        s = Solution()
        self.assertEqual(s.shuffle(nums, n), [2, 3, 5, 4, 1, 7])

    def test_shuffle2(self):
        """
        1470. Shuffle the Array
        """
        nums = [1, 2, 3, 4, 4, 3, 2, 1]
        n = 4
        s = Solution()
        self.assertEqual(s.shuffle(nums, n), [1, 4, 2, 3, 3, 2, 4, 1])

    def test_shuffle3(self):
        """
        1470. Shuffle the Array
        """
        nums = [1, 1, 2, 2]
        n = 2
        s = Solution()
        self.assertEqual(s.shuffle(nums, n), [1, 2, 1, 2])

    def test_sortedSquares1(self):
        # TODOC: Problem number.
        nums = [-4, -1, 0, 3, 10]
        s = Solution()
        self.assertEqual(s.sortedSquares(nums), [0, 1, 9, 16, 100])

    def test_sortedSquares2(self):
        # TODOC: Problem number.
        nums = [-7, -3, 2, 3, 11]
        s = Solution()
        self.assertEqual(s.sortedSquares(nums), [4, 9, 9, 49, 121])


if __name__ == '__main__':
    unittest.main()
