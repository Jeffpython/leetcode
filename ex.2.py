# https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3237/
# Find Numbers with Even Number of Digits
# Given an array nums of integers, return how many of them contain an even number of digits.


class Solution:
    def find_numbers(self, nums: list[int]) -> int:
        number_even_numbers = 0

        for num in nums:
            if len(str(num)) % 2 == 0:
                number_even_numbers += 1

        return number_even_numbers
