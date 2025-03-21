# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr = head
        ans  = k * [None]
        size = 0

        while curr is not None:
            curr = curr.next
            size += 1
        
        nodes_in_each = size // k
        remaining_nodes = size % k
        curr = head
        prev = curr

        for i in range(k):
            new = curr
            current_size  = nodes_in_each
            if remaining_nodes > 0:
                current_size += 1
                remaining_nodes -= 1
            
            j = 0

            while j < current_size:
                prev = curr
                if curr is not None:
                    curr = curr.next
                j += 1
            
            if prev is not None:
                prev.next = None
            
            ans[i] = new
        

        return ans
