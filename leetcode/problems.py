"""
Contains personal solutions to problems.

485. Max Consecutive Ones
977. Squares of a Sorted Array
1089. Duplicate Zeros
1295. Find Numbers with Even Number of Digits
"""
# For Solution.findNumbers().
# Approach not used due to precision issues.
# from math import floor, log10
from typing import List


class Solution:

    def findMaxConsecutiveOnes(self, nums: List[int]) -> List:
        """
        Count the maximum number of consecutive 1's.

        Parameters
        ----------
        nums : list of int
            Binary array.

        Returns
        -------
        count : int

        Examples
        --------
        >>> nums = [1,1,0,1,1,1]
        >>> s = Solution()
        >>> s.findMaxConsecutiveOnes(nums)
        3

        >>> nums = [1,0,1,1,0,1]
        >>> s = Solution()
        >>> s.findMaxConsecutiveOnes(nums)
        2

        Notes
        -----
        485. Max Consecutive Ones
        """
        count = maxcount = 0
        for num in nums:
            if num == 1:
                count += 1
                if maxcount < count:
                    maxcount = count
            else:
                count = 0
        return maxcount

    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Return the squares of the numbers in non-decreasing order.

        Parameters
        ----------
        nums : list of int
            Array of integers.

        Returns
        -------
        squares : list of int
            The squares sorted in non-decreasing order.

        Examples
        --------
        >>> nums = [-4,-1,0,3,10]
        >>> s = Solution()
        >>> s.sortedSquares(nums)
        [0, 1, 9, 16, 100]

        >>> nums = [-7,-3,2,3,11]
        >>> s = Solution()
        >>> s.sortedSquares(nums)
        [4, 9, 9, 49, 121]

        Notes
        -----
        977. Squares of a Sorted Array
        """
        pass

    def has_even(self, x:int) -> bool:
        """
        Checks if number has an even number of digits.

        Helper method for findNumbers().

        Parameters
        ----------
        x : int
            Number to check.

        Returns
        -------
        res : bool
            Whether number has an even number of digits.

        Examples
        --------
        >>> s = Solution()
        >>> s.has_even(12)
        True

        >>> s = Solution()
        >>> s.has_even(345)
        False
        """
        res = True
        while x:
            res = not res
            x //= 10
        return res

    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Modifies an array in place, duplicating occurrences of zero and
        shifting the remaining elements to the right. Elements beyond
        the length of the original array are not written.

        Parameters
        ----------
        arr : list of int
            Array of integers.

        Returns
        -------
        None

        Examples
        --------
        >>> arr = [1,0,2,3,0,4,5,0]
        >>> s = Solution()
        >>> s.duplicateZeros(arr)
        >>> arr
        [1, 0, 0, 2, 3, 0, 0, 4]

        >>> arr = [1,2,3]
        >>> s = Solution()
        >>> s.duplicateZeros(arr)
        >>> arr
        [1, 2, 3]

        Notes
        -----
        1089. Duplicate Zeros
        """
        pass

    def findNumbers(self, nums: List[int]) -> int:
        """
        Count integers containing an even number of digits.

        Parameters
        ----------
        nums : list of int
            Array of integers.

        Returns
        -------
        count : int
            Count of integers containing an even number of digits.

        Examples
        --------
        >>> nums = [12, 345, 2, 6, 7896]
        >>> s = Solution()
        >>> s.findNumbers(nums)
        2

        >>> nums = [555, 901, 482, 1771]
        >>> s = Solution()
        >>> s.findNumbers(nums)
        1

        >>> nums = [999999999999999]
        >>> s = Solution()
        >>> s.findNumbers(nums)
        0

        Notes
        -----
        1295. Find Numbers with Even Number of Digits
        """
        count = 0
        for num in nums:

            count += self.has_even(num)

#         # math.log10 is inaccurate for powers of 10 plus or minus 1
#         # when the power is greater than 14.
#             digits = floor(log10(num)) + 1
#             if digits % 2 == 0:
#                 count += 1

        return count


if __name__ == '__main__':
    import doctest
    doctest.testmod()