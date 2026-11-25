# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists):
        result = []

        for lst in lists:
            while lst:
                result.append(lst.val)
                lst = lst.next

        result.sort()

        dummy = ListNode(0)
        current = dummy

        for value in result:
            current.next = ListNode(value)
            current = current.next

        return dummy.next
        