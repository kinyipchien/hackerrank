"""
Contains tests to problems.

485. Max Consecutive Ones
977. Squares of a Sorted Array
1089. Duplicate Zeros
1108. Defanging an IP Address
1295. Find Numbers with Even Number of Digits
1480. Running Sum of 1d Array
1672. Richest Customer Wealth
1920. Build Array from Permutation
1929. Concatenation of Array
"""

# Authors: Kin-Yip Chien


# For tests.
import unittest

import sys
sys.path.append('..')

from leetcode.problems import Solution


class TestSolution(unittest.TestCase):

    def test_findMaxConsecutiveOnes1(self):
        nums = [1,1,0,1,1,1]
        s = Solution()
        self.assertEqual(s.findMaxConsecutiveOnes(nums), 3)

    def test_findMaxConsecutiveOnes2(self):
        nums = [1,0,1,1,0,1]
        s = Solution()
        self.assertEqual(s.findMaxConsecutiveOnes(nums), 2)

    def test_sortedSquares1(self):
        nums = [-4,-1,0,3,10]
        s = Solution()
        self.assertEqual(s.sortedSquares(nums), [0,1,9,16,100])

    def test_sortedSquares2(self):
        nums = [-7,-3,2,3,11]
        s = Solution()
        self.assertEqual(s.sortedSquares(nums), [4,9,9,49,121])

    def test_duplicateZeros1(self):
        arr = [1,0,2,3,0,4,5,0]
        s = Solution()
        s.duplicateZeros(arr)
        self.assertEqual(arr, [1,0,0,2,3,0,0,4])

    def test_duplicateZeros2(self):
        arr = [1,2,3]
        s = Solution()
        s.duplicateZeros(arr)
        self.assertEqual(arr, [1,2,3])

    def test_findNumbers1(self):
        nums = [12, 345, 2, 6, 7896]
        s = Solution()
        self.assertEqual(s.findNumbers(nums), 2)

    def test_findNumbers2(self):
        nums = [555, 901, 482, 1771]
        s = Solution()
        self.assertEqual(s.findNumbers(nums), 1)

    def test_findNumbers3(self):
        nums = [999999999999999]
        s = Solution()
        self.assertEqual(s.findNumbers(nums), 0)


if __name__ == '__main__':
    unittest.main()
