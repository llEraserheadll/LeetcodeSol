# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        ptr = dummy

        def list_reverse(head,k):
            curr = head
            prev = None
            next = None

            for _ in range(k):
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev,curr

        while ptr != None:
            tracker = ptr

            for i in range(k):
                if tracker == None:
                    break
                
                tracker = tracker.next
            
            if tracker == None:
                break
            
            prev,curr = list_reverse(ptr.next,k)

            last_node = ptr.next
            last_node.next = curr
            ptr.next = prev
            ptr = last_node
        return dummy.next
            

        