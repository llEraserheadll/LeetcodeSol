# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitCircularLinkedList(self, list: Optional[ListNode]) -> List[Optional[ListNode]]:

        if not list:
            return [[],[]]
        slow = list
        fast = list

        while fast.next != list and fast.next.next != list:
            slow = slow.next
            fast = fast.next.next
        
        head1 = list
        head2  = slow.next
        slow.next = head1

        fast = head2

        while fast.next!= list:
            fast = fast.next
        fast.next = head2
    
        return [head1,head2]
        