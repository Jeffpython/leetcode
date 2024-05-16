# https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3240/
# Squares of a Sorted Array
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.


class Solution:
    def sorted_squares(self, nums: list[int]) -> list[int]:
        result = [num ** 2 for num in nums]
        return sorted(result)
