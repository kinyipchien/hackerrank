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
1828. Queries on Number of Points Inside a Circle
"""
from typing import List


class Solution:

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


if __name__ == '__main__':
    import doctest
    doctest.testmod()
