"""
Day 7   6/29/2021
Problem: https://leetcode.com/problems/max-consecutive-ones-iii/

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the
array if you can flip at most k 0's.
 """


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        stack = []
        max_count = 0

        for num in nums:
            stack.append(num)
            if num == 0:
                k -= 1
                while k < 0:
                    if stack.pop(0) == 0:
                        k += 1

            max_count = max(max_count, len(stack))
        return max_count

    def longestOnes_2(self, nums: list[int], k: int) -> int:
        start = 0
        for end in range(len(nums)):
            k = k - (1 - nums[end])
            if k < 0:
                k = k + (1 - nums[start])
                start = start + 1
        return end - start + 1


if __name__ == "__main__":
    test = Solution()
    print(test.longestOnes_2([0,0,0,1], 2))