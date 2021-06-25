"""
Day 3   6/24/2021-Thursday
Problem: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
"""


class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix[0])
        row = [0] * n
        count = 0
        for i in range(n):
            matrix[i].append(int(1e10))

        while True:
            column = [matrix[i][row[i]] for i in range(n)]
            min_val = min(column)
            row[column.index(min_val)] += 1

            count += 1
            if count == k:
                break

        return min_val


test = Solution()
print(test.kthSmallest([[1,1,9],[10,11,13],[12,13,15]], 4))




