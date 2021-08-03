"""
Contains personal solutions to problems.

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
# TODO:
# 1470. Shuffle the Array
# 1431. Kids With the Greatest Number of Candies
# 1512. Number of Good Pairs
# 771. Jewels and Stones
# 1295. Find Numbers with Even Number of Digits
# 977. Squares of a Sorted Array
# 485. Max Consecutive Ones
# 1089. Duplicate Zeros
# 1. Two Sum

# Authors: Kin-Yip Chien

# For Solution.findNumbers().
# Approach not used due to precision issues.
# from math import floor, log10
from typing import List


class Solution:

    def buildArray(self, nums: List[int]) -> List[int]:
        """
        Given a **zero-based permutation** `nums` (**0-indexed**),
        build an array `ans` of the **same length** where
        `ans[i] = nums[nums[i]]` for each `0 <= i < nums.length` and
        return it.

        A **zero-based permutation** `nums` is an array of **distinct**
        integers from `0` to `nums.length - 1` (**inclusive**).

        Parameters
        ----------
        nums : list of int
            Zero-based permutation.

        Returns
        -------
        ans : list of int
            Output array.

        Examples
        --------
        >>> nums = [0, 2, 1, 5, 3, 4]
        >>> s = Solution()
        >>> s.buildArray(nums)
        [0, 1, 2, 4, 5, 3]

        >>> nums = [5, 0, 1, 2, 3, 4]
        >>> s = Solution()
        >>> s.buildArray(nums)
        [4, 5, 0, 1, 2, 3]

        Notes
        -----
        1920. Build Array from Permutation

        Constraints:
        * `1 <= nums.length <= 1000`
        * `0 <= nums[i] < nums.length`
        * The elements in `nums` are **distinct.**
        """
        # TODO: O(n) Time, O(1) Space.

        # O(n) Time, O(n) Space.
        return [nums[num] for num in nums]

    def defangIPaddr(self, address: str) -> str:
        """
        Given a valid (IPv4) IP `address`, return a defanged version of
        that IP address.

        A *defanged IP address* replaces every period `"."` with
        `"[.]"`.

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
        >>> address = "1.1.1.1"
        >>> s = Solution()
        >>> s.defangIPaddr(address)
        '1[.]1[.]1[.]1'

        >>> address = "255.100.50.0"
        >>> s = Solution()
        >>> s.defangIPaddr(address)
        '255[.]100[.]50[.]0'

        Notes
        -----
        1108. Defanging an IP Address
        """
        # O(n * (m1 + m2/m1)) Time, O(n) Space.
        # n : length of the string
        # m1 : length of the searched for string.
        # m2 : length of the replacement.
        return address.replace('.', '[.]')

    def duplicateZeros(self, arr: List[int]) -> None:
        # TODOC: Constraints.
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
        # TODO: O(?) Time, O(?) Space.
        zeros = arr.count(0)
        n = len(arr)
        for i in range(n - 1, -1, -1):
            if zeros == 0:
                break
            if i + zeros < n:
                arr[i + zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < n:
                    arr[i + zeros] = arr[i]

    def findMaxConsecutiveOnes(self, nums: List[int]) -> List:
        # TODOC: Constraints.
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
        # TODO: O(?) Time, O(?) Space.
        count = maxcount = 0
        for num in nums:
            if num == 1:
                count += 1
                maxcount = max(maxcount, count)
            else:
                count = 0
        return maxcount

    def _has_even(self, x:int) -> bool:
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
        """
        res = True
        while x:
            res = not res
            x //= 10
        return res

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

            count += self._has_even(num)

#         # math.log10 is inaccurate for powers of 10 plus or minus 1
#         # when the power is greater than 14.
#             digits = floor(log10(num)) + 1
#             if digits % 2 == 0:
#                 count += 1

        return count
