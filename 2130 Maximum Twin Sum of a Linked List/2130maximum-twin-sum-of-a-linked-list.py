# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        next = None
        curr = slow

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        

        curr = head
        max_sum = 0

        while prev is not None:
            max_sum = max(max_sum,curr.val+prev.val)
            curr = curr.next
            prev = prev.next
        
        return max_sum

        

        