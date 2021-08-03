"""
Contains personal solutions to problems.

485. Max Consecutive Ones
977. Squares of a Sorted Array
1089. Duplicate Zeros
1108. Defanging an IP Address
1295. Find Numbers with Even Number of Digits
1470. Shuffle the Array
1480. Running Sum of 1d Array
1672. Richest Customer Wealth
1920. Build Array from Permutation
1929. Concatenation of Array
"""
# TODO:
# 1431. Kids With the Greatest Number of Candies
# 1512. Number of Good Pairs
# 771. Jewels and Stones
# 1295. Find Numbers with Even Number of Digits
# 977. Squares of a Sorted Array
# 485. Max Consecutive Ones
# 1089. Duplicate Zeros

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
        # TODOC: Constraints.
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
        # TODO: O(?) Time, O(?) Space.
        count = 0
        for num in nums:
#         # math.log10 is inaccurate for powers of 10 plus or minus 1
#         # when the power is greater than 14.
#             digits = floor(log10(num)) + 1
#             if digits % 2 == 0:
#                 count += 1

            count += self._has_even(num)
        return count

    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        Given an integer array `nums` of length `n`, you want to create
        an array `ans` of length `2n` where `ans[i] == nums[i]` and
        `ans[i + n] == nums[i]` for `0 <= i < n` (**0-indexed**).

        Specifically, `ans` is the **concatenation** of two `nums`
        arrays.

        Return *the array* `ans`.

        Parameters
        ----------
        nums : list of int
            Integer array.

        Returns
        -------
        ans : list of int
            Concatenated array.

        Examples
        --------
        >>> nums = [1, 2, 1]
        >>> s = Solution()
        >>> s.getConcatenation(nums)
        [1, 2, 1, 1, 2, 1]

        >>> nums = [1, 3, 2, 1]
        >>> s = Solution()
        >>> s.getConcatenation(nums)
        [1, 3, 2, 1, 1, 3, 2, 1]

        Notes
        -----
        1929. Concatenation of Array

        Constraints:
        * `n == nums.length`
        * `1 <= n <= 1000`
        * `1 <= nums[i] <= 1000`
        """
        # O(n) Time, O(n) Space.
        return nums + nums

    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """
        You are given an `m x n` integer grid `accounts` where
        `accounts[i][j]` is the amount of money the `ith` customer has
        in the `jth` bank. Return *the **wealth** that the richest
        customer has*.

        A customer's **wealth** is the amount of money they have in all
        their bank accounts. The richest customer is the customer that
        has the maximum **wealth**.

        Parameters
        ----------
        accounts : list of list of int
            Matrix of money held by each customer in each bank.

        Returns
        -------
        int
            Wealth of the richest customer.

        Examples
        --------
        >>> accounts = [[1, 2, 3], [3, 2, 1]]
        >>> s = Solution()
        >>> s.maximumWealth(accounts)
        6

        >>> accounts = [[1, 5], [7, 3], [3, 5]]
        >>> s = Solution()
        >>> s.maximumWealth(accounts)
        10

        >>> accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
        >>> s = Solution()
        >>> s.maximumWealth(accounts)
        17

        Notes
        -----
        1672. Richest Customer Wealth

        Constraints:
        * `m == accounts.length`
        * `n == accounts[i].length`
        * `1 <= m, n <= 50`
        * `1 <= accounts[i][j] <= 100`
        """
        # O(m*n) Time, O(1) Space.
        return max(map(sum, accounts))

    def runningSum(self, nums: List[int]) -> List[int]:
        """
        Given an array `nums`. We define a running sum of an array as
        `runningSum[i] = sum(nums[0]…nums[i])`.

        Return the running sum of `nums`.

        Parameters
        ----------
        nums : list of int
            Array.

        Returns
        -------
        running_sum : list of int
            Running sum array.

        Examples
        --------
        >>> nums = [1, 2, 3, 4]
        >>> s = Solution()
        >>> s.runningSum(nums)
        [1, 3, 6, 10]

        >>> nums = [1, 1, 1, 1, 1]
        >>> s = Solution()
        >>> s.runningSum(nums)
        [1, 2, 3, 4, 5]

        >>> nums = [3, 1, 2, 10, 1]
        >>> s = Solution()
        >>> s.runningSum(nums)
        [3, 4, 6, 16, 17]

        Notes
        -----
        1480. Running Sum of 1d Array

        Constraints:
        * `1 <= nums.length <= 1000`
        * `-10^6 <= nums[i] <= 10^6`
        """
        # O(n) Time, O(n) Space.
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums

    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Return the squares of the numbers in non-decreasing order.

        Parameters
        ----------
        nums : list of int
            Array of integers.

        Returns
        -------
        sorted_squares : list of int
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
        sorted_squares = [0] * len(nums)
        left_read_pointer = 0
        right_read_pointer = write_pointer = len(nums) - 1
        left_square = nums[left_read_pointer] ** 2
        right_square = nums[right_read_pointer] ** 2
        while write_pointer >= 0:
            if left_square > right_square:
                sorted_squares[write_pointer] = left_square
                left_read_pointer += 1
                left_square = nums[left_read_pointer] ** 2
            else:
                sorted_squares[write_pointer] = right_square
                right_read_pointer -= 1
                right_square = nums[right_read_pointer] ** 2
            write_pointer -= 1
        return sorted_squares


if __name__ == '__main__':
    import doctest
    doctest.testmod()
