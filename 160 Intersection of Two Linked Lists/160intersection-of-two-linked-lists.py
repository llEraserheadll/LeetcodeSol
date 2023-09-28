# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        # Check if either of the input linked lists is empty
        if not headA or not headB:
            return None

        # Calculate the lengths of both linked lists
        length_headA = self.getLength(headA)
        length_headB = self.getLength(headB)

        # Calculate the difference in lengths
        diff = abs(length_headA - length_headB)

        # Move the pointer of the longer linked list ahead by 'diff' nodes
        if length_headA > length_headB:
            for _ in range(diff):
                headA = headA.next
        else:
            for _ in range(diff):
                headB = headB.next

        # Traverse both linked lists until they intersect
        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headA

    def getLength(self, head):
        """
        Helper function to calculate the length of a linked list.
        """
        length = 0
        while head:
            length += 1
            head = head.next
        return length
