# https://leetcode.com/problems/merge-two-sorted-lists/
# 21. Merge Two Sorted Lists

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two
# lists.
# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]


from copy import deepcopy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_two_lists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        result = []

        while list1:
            result.append(list1.val)
            list1 = list1.next

        while list2:
            result.append(list2.val)
            list2 = list2.next

        result.sort()
        result.reverse()
        list_node = None

        for i in result:
            if list_node:
                list_node.next = deepcopy(list_node)
            else:
                list_node = ListNode(val=i, next=None)

            list_node.val = i

        return list_node
