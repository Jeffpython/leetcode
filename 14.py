# https://leetcode.com/problems/longest-common-prefix/
# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

class Solution:
    def longest_common_prefix(self, strs: list[str]) -> str:
        common_prefix = ""

        for i in range(len(strs[0])):
            test_prefix = strs[0][0:i+1]
            find_count = 0

            for elem in strs:
                if elem.find(test_prefix) == 0:
                    find_count += 1

            if find_count == len(strs):
                common_prefix = test_prefix

        return common_prefix
