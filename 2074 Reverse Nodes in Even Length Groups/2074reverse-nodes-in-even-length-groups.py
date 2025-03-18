# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        l = 2

        while prev.next:
        
            tracker = prev
            n = 0
            for _ in range(l):
                if not tracker.next:
                    break
                
                n += 1
                tracker = tracker.next

            if n % 2 :
                prev = tracker
            else: 
                reverse = tracker.next
                curr = prev.next

                for j in range(n):
                    temp = curr.next
                    curr.next = reverse
                    reverse = curr
                    curr = temp
                
                next_node = prev.next
                prev.next = tracker
                prev = next_node
            l += 1
        return head
        