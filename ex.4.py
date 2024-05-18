# https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3245/
# Duplicate Zeros
# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
# Note: that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.


class Solution:
    def duplicate_zeros(self, arr: list[int]) -> None:
        arr_len = len(arr)
        temp = []

        for i in arr:
            if i == 0:
                temp.append(i)

            temp.append(i)

        arr.clear()

        for i in range(arr_len):
            arr.append(temp[i])
