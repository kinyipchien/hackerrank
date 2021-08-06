# TODO: Move classes to separate modules.
"""
Contains personal solutions to LeetCode problems.

485. Max Consecutive Ones
771. Jewels and Stones
977. Squares of a Sorted Array
1089. Duplicate Zeros
1108. Defanging an IP Address
1295. Find Numbers with Even Number of Digits
1365. How Many Numbers Are Smaller Than the Current Number
1431. Kids With the Greatest Number of Candies
1470. Shuffle the Array
1476. Subrectangle Queries
1480. Running Sum of 1d Array
1512. Number of Good Pairs
1528. Shuffle String
1603. Design Parking System
1672. Richest Customer Wealth
1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
1720. Decode XORed Array
1828. Queries on Number of Points Inside a Circle
1920. Build Array from Permutation
1929. Concatenation of Array
"""

# Authors: Kin-Yip Chien

from typing import List


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
    1603. Design Parking System

    Constraints:
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


class Solution:

    def buildArray(self, nums: List[int]) -> List[int]:
        """
        Builds an array from a zero-based permutation where
        `ans[i] = nums[nums[i]]` for each `0 <= i < nums.length`.

        Parameters
        ----------
        nums : list of int
            Zero-based permutation. An array of **distinct** integers
            from `0` to `nums.length - 1` (**inclusive**).

        Returns
        -------
        ans : list of int
            Output array.

        Examples
        --------
        >>> soln = Solution()
        >>> nums = [0, 2, 1, 5, 3, 4]
        >>> soln.buildArray(nums)
        [0, 1, 2, 4, 5, 3]

        >>> soln = Solution()
        >>> nums = [5, 0, 1, 2, 3, 4]
        >>> soln.buildArray(nums)
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

    def _in_circle(self, point: List[int], circle: List[int]) -> bool:
        """
        Checks if a point is in a circle.

        Helper method for countPoints().

        Parameters
        ----------
        point : list of int
            Cartesian coordinates (x, y) of point.
        circle : list of int
            Cartesian coordinates (h, k) of the center of the circle
            and the radius r as [h, k, r].

        Returns
        -------
        bool
            Whether the point is in the circle.
        """
        x, y = point
        h, k, r = circle
        return ((x - h)**2 + (y - k)**2) <= r**2

    def countPoints(
        self, points: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        """
        Given an array of points and an array of queries, for each
        query, compute the number of points **inside** the `jth`
        circle.

        Points **on the border** of the circle are considered
        **inside**.

        Parameters
        ----------
        points : list of list of int
            An array `points` where `points[i] = [xi, yi]` is the
            coordinates of the `ith` point on a 2D plane.
        queries : list of list of int
            An array `queries` where `queries[j] = [xj, yj, rj]`
            describes a circle centered at `(xj, yj)` with a radius of
            `rj`.

        Returns
        -------
        array
            *An array where `array[j]` is the answer to the `jth`
            query*.

        Examples
        --------
        >>> soln = Solution()
        >>> points = [[1, 3], [3, 3], [5, 3], [2, 2]]
        >>> queries = [[2, 3, 1], [4, 3, 1], [1, 1, 2]]
        >>> soln.countPoints(points, queries)
        [3, 2, 2]

        >>> soln = Solution()
        >>> points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
        >>> queries = [[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]]
        >>> soln.countPoints(points, queries)
        [2, 3, 2, 4]

        Notes
        -----
        1828. Queries on Number of Points Inside a Circle

        Constraints:
        * `1 <= points.length <= 500`
        * `points[i].length == 2`
        * `0 <= xi, yi <= 500`
        * `1 <= queries.length <= 500`
        * `queries[j].length == 3`
        * `0 <= xj, yj <= 500`
        * `1 <= rj <= 500`
        * All coordinates are integers.
        """
        # RFE: k-d tree.

        # O(m*n) Time, O(n) Space.
        return [sum(self._in_circle(point, query) for point in points)
                for query in queries]

    def decode(self, encoded: List[int], first: int) -> List[int]:
        """
        Decodes an encoded array.

        An integer array that consists of `n` non-negative integers is
        encoded into another integer array of length `n - 1`, such that
        `encoded[i] = arr[i] XOR arr[i + 1]`. For example, if
        `arr = [1,0,2,1]`, then `encoded = [1,2,3]`.

        Parameters
        ----------
        encoded : list of int
            Encoded array.
        first : int
            First element of decoded array.

        Returns
        -------
        decoded : list of int
            Decoded array.

        Examples
        --------
        >>> soln = Solution()
        >>> encoded = [1, 2, 3]
        >>> first = 1
        >>> soln.decode(encoded, first)
        [1, 0, 2, 1]

        >>> soln = Solution()
        >>> encoded = [6, 2, 7, 3]
        >>> first = 4
        >>> soln.decode(encoded, first)
        [4, 2, 0, 7, 4]

        Notes
        -----
        1720. Decode XORed Array

        Constraints:
        * `2 <= n <= 10^4`
        * `encoded.length == n - 1`
        * `0 <= encoded[i] <= 10^5`
        * `0 <= first <= 10^5`
        """
        # O(n) Time, O(n) Space.
        decoded = [first]
        for elem in encoded:
            decoded.append(decoded[-1] ^ elem)
        return decoded

    def defangIPaddr(self, address: str) -> str:
        """
        Defangs a (IPv4) IP `address` by replacing every period `"."`
        with `"[.]"`.

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
        >>> soln = Solution()
        >>> address = "1.1.1.1"
        >>> soln.defangIPaddr(address)
        '1[.]1[.]1[.]1'

        >>> soln = Solution()
        >>> address = "255.100.50.0"
        >>> soln.defangIPaddr(address)
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
        Duplicates each occurrence of zero in an input array in-place,
        shifting the remaining elements to the right.

        Elements beyond the length of the original array are
        not written.

        Parameters
        ----------
        arr : list of int
            Array of integers.

        Returns
        -------
        None

        Examples
        --------
        >>> soln = Solution()
        >>> arr = [1, 0, 2, 3, 0, 4, 5, 0]
        >>> soln.duplicateZeros(arr)
        >>> arr
        [1, 0, 0, 2, 3, 0, 0, 4]

        >>> soln = Solution()
        >>> arr = [1, 2, 3]
        >>> soln.duplicateZeros(arr)
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
        """
        Returns *the maximum number of consecutive `1`'s in the array*.

        Parameters
        ----------
        nums : list of int
            Binary array.

        Returns
        -------
        max_ones : int
            Maximum number of consecutive ones in the array.

        Examples
        --------
        >>> soln = Solution()
        >>> nums = [1, 1, 0, 1, 1, 1]
        >>> soln.findMaxConsecutiveOnes(nums)
        3

        >>> soln = Solution()
        >>> nums = [1, 0, 1, 1, 0, 1]
        >>> soln.findMaxConsecutiveOnes(nums)
        2

        Notes
        -----
        485. Max Consecutive Ones

        Constraints:
        * `1 <= nums.length <= 10^5`
        * `nums[i]` is either `0` or `1`.
        """
        # O(n) Time, O(1) Space.
        ones = max_ones = 0
        for num in nums:
            ones = ones * num + num
            max_ones = max(ones, max_ones)
        return max_ones

    def _has_even_num_digits(self, num:int) -> bool:
        """
        Checks if a number has an even number of digits.

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
        while num >= 10:
            even_num_digits = not even_num_digits
            num //= 10
        return even_num_digits

    def findNumbers(self, nums: List[int]) -> int:
        """
        Returns how many numbers in an input array contain an **even
        number** of digits.

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
        >>> soln = Solution()
        >>> nums = [12, 345, 2, 6, 7896]
        >>> soln.findNumbers(nums)
        2

        >>> soln = Solution()
        >>> nums = [555, 901, 482, 1771]
        >>> soln.findNumbers(nums)
        1

        >>> soln = Solution()
        >>> nums = [999999999999999]
        >>> soln.findNumbers(nums)
        0

        >>> soln = Solution()
        >>> nums = [100000]
        >>> soln.findNumbers(nums)
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
        Returns the concatenation of an array with itself.

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
        >>> soln = Solution()
        >>> nums = [1, 2, 1]
        >>> soln.getConcatenation(nums)
        [1, 2, 1, 1, 2, 1]

        >>> soln = Solution()
        >>> nums = [1, 3, 2, 1]
        >>> soln.getConcatenation(nums)
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
        Returns a boolean array denoting whether each of n kids has the
        greatest number of candies.

        A kid has the greatest number of candies if they have the most
        candies among the kids after receiving all the extraCandies.

        Note that multiple kids can have the greatest number of
        candies.

        Parameters
        ----------
        candies : list of int
            An integer array, where each `candies[i]` represents the
            number of candies the `ith` kid has.
        extraCandies : int
            Number of extra candies that you have.

        Returns
        -------
        list of bool
            Whether each kid has the greatest number of candies.
            `result[i]` is `true` if, after giving the `ith` kid all
            the `extraCandies`, they will have the **greatest number**
            of candies among all the kids, or `false` otherwise*

        Examples
        --------
        >>> soln = Solution()
        >>> candies = [2, 3, 5, 1, 3]
        >>> extraCandies = 3
        >>> soln.kidsWithCandies(candies, extraCandies)
        [True, True, True, False, True]

        >>> soln = Solution()
        >>> candies = [4, 2, 1, 1, 2]
        >>> extraCandies = 1
        >>> soln.kidsWithCandies(candies, extraCandies)
        [True, False, False, False, False]

        >>> soln = Solution()
        >>> candies = [12, 1, 12]
        >>> extraCandies = 10
        >>> soln.kidsWithCandies(candies, extraCandies)
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
        Returns *the **wealth** that the richest customer has*.

        A customer's **wealth** is the amount of money they have in all
        their bank accounts. The richest customer is the customer that
        has the maximum **wealth**.

        Parameters
        ----------
        accounts : list of list of int
            `m x n` integer grid where `accounts[i][j]` is the amount
            of money the `ith` customer has in the `jth` bank.

        Returns
        -------
        int
            Wealth of the richest customer.

        Examples
        --------
        >>> soln = Solution()
        >>> accounts = [[1, 2, 3], [3, 2, 1]]
        >>> soln.maximumWealth(accounts)
        6

        >>> soln = Solution()
        >>> accounts = [[1, 5], [7, 3], [3, 5]]
        >>> soln.maximumWealth(accounts)
        10

        >>> soln = Solution()
        >>> accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
        >>> soln.maximumWealth(accounts)
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

    def minPartitions(self, n: str) -> int:
        """
        Returns the **minimum** number of positive **deci-binary**
        numbers needed to sum up to `n`*.

        A decimal number is called **deci-binary** if each of its
        digits is either `0` or `1` without any leading zeros. For
        example, `101` and `1100` are **deci-binary**, while `112` and
        `3001` are not.

        Parameters
        ----------
        n : str
            String representing a positive decimal integer.

        Returns
        -------
        int
            **Minimum** number of positive **deci-binary** numbers
            needed to sum up to `n`*.

        Examples
        --------
        >>> soln = Solution()
        >>> n = "32"
        >>> soln.minPartitions(n)
        3

        >>> soln = Solution()
        >>> n = "82734"
        >>> soln.minPartitions(n)
        8

        >>> soln = Solution()
        >>> n = "27346209830709182346"
        >>> soln.minPartitions(n)
        9

        Notes
        -----
        1689. Partitioning Into Minimum Number Of Deci-Binary Numbers

        Constraints
        * `1 <= n.length <= 10^5`
        * `n` consists of only digits.
        * `n` does not contain any leading zeros and represents a
        positive integer.
        """
        # O(n) Time, O(1) Space.
        return int(max(n))

    def numIdenticalPairs(self, nums: List[int]) -> int:
        """
        Return the number of *good* pairs given an array of integers.

        A pair `(i,j)` is called *good* if `nums[i]` == `nums[j]` and
        `i` < `j`.

        Parameters
        ----------
        nums : list of int
            Array of integers.

        Returns
        -------
        pairs : int
            Number of good pairs.

        Examples
        --------
        >>> soln = Solution()
        >>> nums = [1, 2, 3, 1, 1, 3]
        >>> soln.numIdenticalPairs(nums)
        4

        >>> soln = Solution()
        >>> nums = [1, 1, 1, 1]
        >>> soln.numIdenticalPairs(nums)
        6

        >>> soln = Solution()
        >>> nums = [1, 2, 3]
        >>> soln.numIdenticalPairs(nums)
        0

        Notes
        -----
        1512. Number of Good Pairs

        Constraints:
        * `1 <= nums.length <= 100`
        * `1 <= nums[i] <= 100`
        """
        # O(n) Time. O(n) Space.
        c = {}
        pairs = 0
        for num in nums:
            if num in c:
                pairs += c[num]
                c[num] += 1
            else:
                c[num] = 1
        return pairs

    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """
        Computes how many of the stones you have are also jewels.

        Parameters
        ----------
        jewels : str
            String representing the types of stones that are jewels.
            Letters are case sensitive.
        stones : str
            String representing the stones you have. Letters are case
            sensitive.

        Returns
        -------
        int
            Number of jewels you have.

        Examples
        --------
        >>> soln = Solution()
        >>> jewels = "aA"
        >>> stones = "aAAbbbb"
        >>> soln.numJewelsInStones(jewels, stones)
        3

        >>> soln = Solution()
        >>> jewels = "z"
        >>> stones = "ZZ"
        >>> soln.numJewelsInStones(jewels, stones)
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

    def restoreString(self, s: str, indices: List[int]) -> str:
        """
        Shuffle a string such that the character at the `ith` position
        moves to the `indices[i]` position.

        Parameters
        ----------
        s : str
            String.
        indices : list of int
            Integer array.

        Returns
        -------
        str
            Shuffled string.

        Examples
        --------
        >>> soln = Solution()
        >>> s = "codeleet"
        >>> indices = [4, 5, 6, 7, 0, 2, 1, 3]
        >>> soln.restoreString(s, indices)
        'leetcode'

        >>> soln = Solution()
        >>> s = "abc"
        >>> indices = [0,1,2]
        >>> soln.restoreString(s, indices)
        'abc'

        >>> soln = Solution()
        >>> s = "aiohn"
        >>> indices = [3, 1, 4, 2, 0]
        >>> soln.restoreString(s, indices)
        'nihao'

        >>> soln = Solution()
        >>> s = "aaiougrt"
        >>> indices = [4, 0, 2, 6, 7, 3, 1, 5]
        >>> soln.restoreString(s, indices)
        'arigatou'

        >>> soln = Solution()
        >>> s = "art"
        >>> indices = [1, 0, 2]
        >>> soln.restoreString(s, indices)
        'rat'

        Notes
        -----
        1528. Shuffle String

        Constraints:
        * `s.length == indices.length == n`
        * `1 <= n <= 100`
        * `s` contains only lower-case English letters.
        * `0 <= indices[i] < n`
        * All values of `indices` are unique (i.e. `indices` is a
        permutation of the integers from `0` to `n - 1`).
        """
        # O(n) Time, O(n) Space.
        restored = [''] * len(s)
        for i, idx in enumerate(indices):
            restored[idx] = s[i]
        return ''.join(restored)

    def runningSum(self, nums: List[int]) -> List[int]:
        """
        Returns the running sum of an array where
        `runningSum[i] = sum(nums[0]…nums[i])`.

        Parameters
        ----------
        nums : list of int
            Array.

        Returns
        -------
        running_sum : list of int
            Running sum.

        Examples
        --------
        >>> soln = Solution()
        >>> nums = [1, 2, 3, 4]
        >>> soln.runningSum(nums)
        [1, 3, 6, 10]

        >>> soln = Solution()
        >>> nums = [1, 1, 1, 1, 1]
        >>> soln.runningSum(nums)
        [1, 2, 3, 4, 5]

        >>> soln = Solution()
        >>> nums = [3, 1, 2, 10, 1]
        >>> soln.runningSum(nums)
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
        Given an array in the form `[x1,x2,...,xn,y1,y2,...,yn]`,
        returns an array in the form `[x1,y1,x2,y2,...,xn,yn]`.

        Parameters
        ----------
        nums : list of int
            Integer array consisting of `2n` elements in the form
            `[x1,x2,...,xn,y1,y2,...,yn]`.
        n : int
            Positive integer.

        Returns
        -------
        shuffled : list of int
            Shuffled array in the form `[x1,y1,x2,y2,...,xn,yn]`.

        Examples
        --------
        >>> soln = Solution()
        >>> nums = [2, 5, 1, 3, 4, 7]
        >>> n = 3
        >>> soln.shuffle(nums, n)
        [2, 3, 5, 4, 1, 7]

        >>> soln = Solution()
        >>> nums = [1, 2, 3, 4, 4, 3, 2, 1]
        >>> n = 4
        >>> soln.shuffle(nums, n)
        [1, 4, 2, 3, 3, 2, 4, 1]

        >>> soln = Solution()
        >>> nums = [1, 1, 2, 2]
        >>> n = 2
        >>> soln.shuffle(nums, n)
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
        shuffled = [None] * 2*n
        shuffled[::2], shuffled[1::2] = nums[:n], nums[n:]
        return shuffled

    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """
        For a given array `nums`, returns an array where `array[i]` is
        how many numbers in the array are smaller than `nums[i]`.

        Parameters
        ----------
        nums : list of int
            Integer array.

        Returns
        -------
        list of int
            Result array.

        Examples
        --------
        >>> soln = Solution()
        >>> nums = [8, 1, 2, 2, 3]
        >>> soln.smallerNumbersThanCurrent(nums)
        [4, 0, 1, 1, 3]

        >>> soln = Solution()
        >>> nums = [6, 5, 4, 8]
        >>> soln.smallerNumbersThanCurrent(nums)
        [2, 1, 0, 3]

        >>> soln = Solution()
        >>> nums = [7,7,7,7]
        >>> soln.smallerNumbersThanCurrent(nums)
        [0, 0, 0, 0]

        Notes
        -----
        1365. How Many Numbers Are Smaller Than the Current Number

        Constraints:
        * `2 <= nums.length <= 500`
        * `0 <= nums[i] <= 100`
        """
        # O(n) Time, O(n) Space.
        count = [0] * (max(nums) + 2)
        for num in nums:
            count[num + 1] += 1
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        return [count[num] for num in nums]

    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Returns an array of the squares of each number in an input
        array, sorted in non-decreasing order.

        Parameters
        ----------
        nums : list of int
            Integer array sorted in non-decreasing order.

        Returns
        -------
        sorted_squares : list of int
            The squares of the input numbers sorted in non-decreasing
            order.

        Examples
        --------
        >>> soln = Solution()
        >>> nums = [-4, -1, 0, 3, 10]
        >>> soln.sortedSquares(nums)
        [0, 1, 9, 16, 100]

        >>> soln = Solution()
        >>> nums = [-7, -3, 2, 3, 11]
        >>> soln.sortedSquares(nums)
        [4, 9, 9, 49, 121]

        Notes
        -----
        977. Squares of a Sorted Array

        Constraints:
        * `1 <= nums.length <= 10^4`
        * `-10^4 <= nums[i] <= 10^4`
        * `nums` is sorted in **non-decreasing** order.
        """
        # O(n) Time, O(n) Space.
        n = len(nums)
        sorted_squares = [None] * n
        left, right = 0, n - 1
        for i in range(n - 1, -1, -1):
            left_squared = nums[left] ** 2
            right_squared = nums[right] ** 2
            if left_squared >= right_squared:
                sorted_squares[i] = left_squared
                left += 1
            else:
                sorted_squares[i] = right_squared
                right -= 1
        return sorted_squares


class SubrectangleQueries:
    """
    The class SubrectangleQueries receives a matrix of integers.

    Parameters
    ----------
    rectangle : list of list of int
        Rows x cols rectangle.

    Examples
    --------
    >>> subrectangleQueries = SubrectangleQueries(
    ...     [[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]])
    >>> subrectangleQueries.getValue(0, 2)
    1
    >>> subrectangleQueries.updateSubrectangle(0, 0, 3, 2, 5)
    >>> subrectangleQueries.rectangle
    [[5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5]]
    >>> subrectangleQueries.getValue(0, 2)
    5
    >>> subrectangleQueries.getValue(3, 1)
    5
    >>> subrectangleQueries.updateSubrectangle(3, 0, 3, 2, 10)
    >>> subrectangleQueries.rectangle
    [[5, 5, 5], [5, 5, 5], [5, 5, 5], [10, 10, 10]]
    >>> subrectangleQueries.getValue(3, 1)
    10
    >>> subrectangleQueries.getValue(0, 2)
    5

    >>> subrectangleQueries = SubrectangleQueries(
    ...     [[1, 1, 1], [2, 2, 2], [3, 3, 3]])
    >>> subrectangleQueries.getValue(0, 0)
    1
    >>> subrectangleQueries.updateSubrectangle(0, 0, 2, 2, 100)
    >>> subrectangleQueries.getValue(0, 0)
    100
    >>> subrectangleQueries.getValue(2, 2)
    100
    >>> subrectangleQueries.updateSubrectangle(1, 1, 2, 2, 20)
    >>> subrectangleQueries.getValue(2, 2)
    20

    Notes
    -----
    1476. Subrectangle Queries

    Constraints:
    * There will be at most `500` operations considering both methods:
    `updateSubrectangle` and `getValue`.
    * `1 <= rows, cols <= 100`
    * `rows == rectangle.length`
    * `cols == rectangle[i].length`
    * `0 <= row1 <= row2 < rows`
    * `0 <= col1 <= col2 < cols`
    * `1 <= newValue, rectangle[i][j] <= 10^9`
    * `0 <= row < rows`
    * `0 <= col < cols`
    """
    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(
        self, row1: int, col1: int, row2: int, col2: int, newValue: int
    ) -> None:
        """
        Updates all values in the subrectangle.

        Parameters
        ----------
        row1 : int
            Row of upper left corner of subrectangle.
        col1 : int
            Column of upper left corner of subrectangle.
        row2 : int
            Row of bottom right corner of subrectangle.
        col2 : int
            Column of bottom right corner of subrectangle.
        newalue : int
            Value to update with.

        Returns
        -------
        None
        """
        # O(n^2) Time, O(1) Space.
        new_row = [newValue] * (col2 - col1 + 1)
        for row in range(row1, row2 + 1):
            self.rectangle[row][col1:col2 + 1] = new_row

    def getValue(self, row: int, col: int) -> int:
        """
        Returns the rectangle value at the coordinate (row, col).

        Parameters
        ----------
        row : int
            Rectangle row.
        col : int
            Rectangle column

        Returns
        -------
        int
            Rectangle value at coordinate.
        """
        # O(1) Time, O(1) Space.
        return self.rectangle[row][col]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
