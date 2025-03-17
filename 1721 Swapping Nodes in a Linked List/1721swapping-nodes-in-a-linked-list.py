# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def swap(node1,node2):
            temp = node1.val
            node1.val = node2.val
            node2.val = temp
        
        front = None
        end = None
        curr= head
        count = 0

        while curr:
            count += 1
            if end is not None:
                end = end.next
            
            if count == k:
                front = curr
                end = head
            curr = curr.next
        
        swap(front,end)

        return head