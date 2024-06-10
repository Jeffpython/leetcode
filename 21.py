from copy import deepcopy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_two_lists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        # print(list1)
        result = []

        while list1 is not None:
            result.append(list1.val)
            list1 = list1.next

        while list2 is not None:
            result.append(list2.val)
            list2 = list2.next

        result.sort()
        result.reverse()
        # print('result', result)

        list_node = ListNode('')

        for i in result:
            if list_node.val:
                list_node.next = deepcopy(list_node)
            else:
                list_node.next = None

            # print('i', i)
            list_node.val = i

        print('list_node', list_node)

        return list_node


