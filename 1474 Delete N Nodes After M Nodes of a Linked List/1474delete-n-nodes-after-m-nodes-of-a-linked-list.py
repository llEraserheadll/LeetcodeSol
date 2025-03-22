# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        curr = head
        prev = head

        while curr:
            m_node = m
            n_node = n

            while curr and m_node > 0:
                prev = curr
                curr = curr.next
                m_node -= 1

            while curr and n_node > 0:
                curr = curr.next
                n_node -= 1
            
            prev.next = curr
        return head
        