# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_list(self,slow):
        prev = None
        curr = slow
        next = None

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
    
    def compare_list(self,first_half,second_half):
        while first_half and second_half:
            if first_half.val != second_half.val:
                return False
            else:
                first_half = first_half.next
                second_half = second_half.next
        
        return True

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
        
        second_half = self.reverse_list(slow)

        check = self.compare_list(head,second_half)

        self.reverse_list(second_half)

        if check:
            return True
        return False
        

        