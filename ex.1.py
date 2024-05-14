# https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/
# Max Consecutive Ones
# Given a binary array nums, return the maximum number of consecutive 1's in the array.


class Solution:
    def find_max_consecutive_ones(self, nums: list[int]) -> int:
        max_consecutive_ones = 0
        current_consecutive_ones = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                if current_consecutive_ones == 0:
                    current_consecutive_ones = 1
                elif i > 0 and nums[i - 1] == 1:
                    current_consecutive_ones += 1

                if current_consecutive_ones > max_consecutive_ones:
                    max_consecutive_ones = current_consecutive_ones
            else:
                current_consecutive_ones = 0

        return max_consecutive_ones
