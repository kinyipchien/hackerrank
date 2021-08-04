"""
Contains personal solutions to LeetCode problems.

485. Max Consecutive Ones
771. Jewels and Stones
977. Squares of a Sorted Array
1089. Duplicate Zeros
1108. Defanging an IP Address
1295. Find Numbers with Even Number of Digits
1431. Kids With the Greatest Number of Candies
1470. Shuffle the Array
1480. Running Sum of 1d Array
1512. Number of Good Pairs
1672. Richest Customer Wealth
1920. Build Array from Permutation
1929. Concatenation of Array
"""

# Authors: Kin-Yip Chien

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
        >>> s = Solution()
        >>> nums = [0, 2, 1, 5, 3, 4]
        >>> s.buildArray(nums)
        [0, 1, 2, 4, 5, 3]

        >>> s = Solution()
        >>> nums = [5, 0, 1, 2, 3, 4]
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
        # RFE: Implement in O(n) Time, O(1) Space.

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
        >>> s = Solution()
        >>> address = "1.1.1.1"
        >>> s.defangIPaddr(address)
        '1[.]1[.]1[.]1'

        >>> s = Solution()
        >>> address = "255.100.50.0"
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
        """
        Given a fixed length array `arr` of integers, duplicate each
        occurrence of zero, shifting the remaining elements to the
        right.

        Note that elements beyond the length of the original array are
        not written.

        Do the above modifications to the input array **in place**, do
        not return anything from your function.

        Parameters
        ----------
        arr : list of int
            Array of integers.

        Returns
        -------
        None

        Examples
        --------
        >>> s = Solution()
        >>> arr = [1, 0, 2, 3, 0, 4, 5, 0]
        >>> s.duplicateZeros(arr)
        >>> arr
        [1, 0, 0, 2, 3, 0, 0, 4]

        >>> s = Solution()
        >>> arr = [1, 2, 3]
        >>> s.duplicateZeros(arr)
        >>> arr
        [1, 2, 3]

        Notes
        -----
        1089. Duplicate Zeros

        * `1 <= arr.length <= 10000`
        * `0 <= arr[i] <= 9`
        """
        # O(n) Time, O(1) Space.
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
        >>> s = Solution()
        >>> nums = [1,1,0,1,1,1]
        >>> s.findMaxConsecutiveOnes(nums)
        3

        >>> s = Solution()
        >>> nums = [1,0,1,1,0,1]
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

    def _has_even_num_digits(self, x:int) -> bool:
        """
        Checks if number has an even number of digits.

        Helper method for findNumbers().

        Parameters
        ----------
        x : int
            Number to check.

        Returns
        -------
        even_num_digits : bool
            Whether number has an even number of digits.
        """
        even_num_digits = False
        while x >= 10:
            even_num_digits = not even_num_digits
            x //= 10
        return even_num_digits

    def findNumbers(self, nums: List[int]) -> int:
        # TODOC: Constraints.
        """
        Given an array `nums` of integers, return how many of them
        contain an **even number** of digits.

        Parameters
        ----------
        nums : list of int
            Array of integers.

        Returns
        -------
        int
            Count of integers containing an even number of digits.

        Examples
        --------
        >>> s = Solution()
        >>> nums = [12, 345, 2, 6, 7896]
        >>> s.findNumbers(nums)
        2

        >>> s = Solution()
        >>> nums = [555, 901, 482, 1771]
        >>> s.findNumbers(nums)
        1

        >>> s = Solution()
        >>> nums = [999999999999999]
        >>> s.findNumbers(nums)
        0

        >>> s = Solution()
        >>> nums = [100000]
        >>> s.findNumbers(nums)
        1

        Notes
        -----
        1295. Find Numbers with Even Number of Digits

        Constraints:
        * `1 <= nums.length <= 500`
        * `1 <= nums[i] <= 10^5`
        """
        # O(nlogn) Time, O(1) Space.
        return sum(self._has_even_num_digits(num) for num in nums)

        # BUG: math.log10 is inaccurate for 1e(x) +/- 1 when x > 14.
#         count_even_num_digits = 0
#         for num in nums:
#             digits = floor(log10(num)) + 1
#             if digits % 2 == 0:
#                 count_even_num_digits += 1
#         return count_even_num_digits

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
        >>> s = Solution()
        >>> nums = [1, 2, 1]
        >>> s.getConcatenation(nums)
        [1, 2, 1, 1, 2, 1]

        >>> s = Solution()
        >>> nums = [1, 3, 2, 1]
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

    def kidsWithCandies(
        self, candies: List[int], extraCandies: int
    ) -> List[bool]:
        """
        There are `n` kids with candies. You are given an integer array
        `candies`, where each `candies[i]` represents the number of
        candies the `ith` kid has, and an integer `extraCandies`,
        denoting the number of extra candies that you have.

        Return a *boolean array `result` of length `n`, where
        `result[i]` is `true` if, after giving the `ith` kid all the
        `extraCandies`, they will have the **greatest number** of
        candies among all the kids, or `false` otherwise*.

        Note that multiple kids can have the greatest number of
        candies.

        Parameters
        ----------
        candies : list of int
            Number of candies each kid has.
        extraCandies : int
            Number of extra candies.

        Returns
        -------
        has_greatest_num_candies : list of bool
            Whether each kid has the greatest number of candies.

        Examples
        --------
        >>> s = Solution()
        >>> candies = [2, 3, 5, 1, 3]
        >>> extraCandies = 3
        >>> s.kidsWithCandies(candies, extraCandies)
        [True, True, True, False, True]

        >>> s = Solution()
        >>> candies = [4, 2, 1, 1, 2]
        >>> extraCandies = 1
        >>> s.kidsWithCandies(candies, extraCandies)
        [True, False, False, False, False]

        >>> s = Solution()
        >>> candies = [12, 1, 12]
        >>> extraCandies = 10
        >>> s.kidsWithCandies(candies, extraCandies)
        [True, False, True]

        Notes
        -----
        1431. Kids With the Greatest Number of Candies

        Constraints:
        * `n == candies.length`
        * `2 <= n <= 100`
        * `1 <= candies[i] <= 100`
        * `1 <= extraCandies <= 50`
        """
        # O(n) Time, O(n) Space.
        threshold = max(candies) - extraCandies
        return [kid >= threshold for kid in candies]

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
        >>> s = Solution()
        >>> accounts = [[1, 2, 3], [3, 2, 1]]
        >>> s.maximumWealth(accounts)
        6

        >>> s = Solution()
        >>> accounts = [[1, 5], [7, 3], [3, 5]]
        >>> s.maximumWealth(accounts)
        10

        >>> s = Solution()
        >>> accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
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

    def numIdenticalPairs(self, nums: List[int]) -> int:
        """
        Given an array of integers `nums`.

        A pair `(i,j)` is called *good* if `nums[i]` == `nums[j]` and `i` < `j`.

        Return the number of *good* pairs.

        Parameters
        ----------
        nums : list of int
            Array of integers.

        Returns
        -------
        num_pairs : int
            Number of good pairs.

        Examples
        --------
        >>> s = Solution()
        >>> nums = [1, 2, 3, 1, 1, 3]
        >>> s.numIdenticalPairs(nums)
        4

        >>> s = Solution()
        >>> nums = [1, 1, 1, 1]
        >>> s.numIdenticalPairs(nums)
        6

        >>> s = Solution()
        >>> nums = [1, 2, 3]
        >>> s.numIdenticalPairs(nums)
        0

        Notes
        -----
        1512. Number of Good Pairs

        Constraints:
        * `1 <= nums.length <= 100`
        * `1 <= nums[i] <= 100`
        """
        # O(n) Time. O(n) Space.
        num_ctr = {}
        num_pairs = 0
        for num in nums:
            if num in num_ctr:
                num_pairs += num_ctr[num]
                num_ctr[num] += 1
            else:
                num_ctr[num] = 1
        return num_pairs

    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """
        You're given strings `jewels` representing the types of stones
        that are jewels, and `stones` representing the stones you have.
        Each character in `stones` is a type of stone you have. You
        want to know how many of the stones you have are also jewels.

        Letters are case sensitive, so `"a"` is considered a different
        type of stone from `"A"`.

        Parameters
        ----------
        jewels : str
            Jewel characters.
        stones : str
            Stones you have.

        Returns
        -------
        int
            Number of jewels you have.

        Examples
        --------
        >>> s = Solution()
        >>> jewels = "aA"
        >>> stones = "aAAbbbb"
        >>> s.numJewelsInStones(jewels, stones)
        3

        >>> s = Solution()
        >>> jewels = "z"
        >>> stones = "ZZ"
        >>> s.numJewelsInStones(jewels, stones)
        0

        Notes
        -----
        771. Jewels and Stones

        Constraints:
        * `1 <= jewels.length, stones.length <= 50`
        * `jewels` and `stones` consist of only English letters.
        * All the characters of `jewels` are **unique**.
        """
        # O(j + s) Time, O(j) Space.
        set_jewels = set(jewels)
        return sum(stone in set_jewels for stone in stones)

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
        >>> s = Solution()
        >>> nums = [1, 2, 3, 4]
        >>> s.runningSum(nums)
        [1, 3, 6, 10]

        >>> s = Solution()
        >>> nums = [1, 1, 1, 1, 1]
        >>> s.runningSum(nums)
        [1, 2, 3, 4, 5]

        >>> s = Solution()
        >>> nums = [3, 1, 2, 10, 1]
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

    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """
        Given the array `nums` consisting of `2n` elements in the form
        `[x1,x2,...,xn,y1,y2,...,yn]`.

        *Return the array in the form* `[x1,y1,x2,y2,...,xn,yn]`.

        Parameters
        ----------
        nums : list of int
            Integer array.
        n : int
            Positive integer.

        Returns
        -------
        shuffled : list of int
            Shuffled array.

        Examples
        --------
        >>> s = Solution()
        >>> nums = [2, 5, 1, 3, 4, 7]
        >>> n = 3
        >>> s.shuffle(nums, n)
        [2, 3, 5, 4, 1, 7]

        >>> s = Solution()
        >>> nums = [1, 2, 3, 4, 4, 3, 2, 1]
        >>> n = 4
        >>> s.shuffle(nums, n)
        [1, 4, 2, 3, 3, 2, 4, 1]

        >>> s = Solution()
        >>> nums = [1, 1, 2, 2]
        >>> n = 2
        >>> s.shuffle(nums, n)
        [1, 2, 1, 2]

        Notes
        -----
        1470. Shuffle the Array

        Constraints:
        * `1 <= n <= 500`
        * `nums.length == 2n`
        * `1 <= nums[i] <= 10^3`
        """
        # O(n) Time, O(n) Space.
        shuffled = []
        for x, y in zip(nums[:n], nums[n:]):
            shuffled += [x, y]
        return shuffled

    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Return the squares of the numbers in non-decreasing order.

        Parameters
        ----------
        nums : list of int
            Integer array.

        Returns
        -------
        sorted_squares : list of int
            The squares sorted in non-decreasing order.

        Examples
        --------
        >>> s = Solution()
        >>> nums = [-4,-1,0,3,10]
        >>> s.sortedSquares(nums)
        [0, 1, 9, 16, 100]

        >>> s = Solution()
        >>> nums = [-7,-3,2,3,11]
        >>> s.sortedSquares(nums)
        [4, 9, 9, 49, 121]

        Notes
        -----
        977. Squares of a Sorted Array
        """
        # TODO: O(?) Time, O(?) Space.
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
