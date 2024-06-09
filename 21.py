class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def merge_two_lists(self, list1: list, list2: list) -> list:



        list1.extend(list2)
        return sorted(list1)


list1 = [1, 2, 4]
list2 = [1, 3, 4]

solution = Solution()
print(solution.merge_two_lists(solution, list1, list2))

