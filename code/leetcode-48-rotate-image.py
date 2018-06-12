"""
https://leetcode.com/problems/rotate-image/description/
Description:
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
"""


class Solution:
    def get_target(self, row, col, n):
        return col, n - row - 1

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        starts = [(sx, sy) for sx in range((n + 1) // 2) for sy in range(sx, n - sx - 1)]
        for start in starts:
            # move around the perimeter
            sx, sy = start
            val = matrix[sx][sy]
            while True:
                tx, ty = self.get_target(sx, sy, n)
                val, matrix[tx][ty] = matrix[tx][ty], val
                sx, sy = tx, ty
                if (sx, sy) == start:
                    break
