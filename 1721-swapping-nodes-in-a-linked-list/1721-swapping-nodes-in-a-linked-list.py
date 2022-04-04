# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p = 1
        start = 0
        end = head
        temp = head
        while(temp):
            if p == k:
                start = temp
            temp = temp.next
            p += 1
            if p > k+1:
                end = end.next
        start.val, end.val = end.val, start.val
        return head
        