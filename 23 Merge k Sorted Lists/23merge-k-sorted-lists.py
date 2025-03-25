# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def merge_2_lists(head1,head2):
#         dummy = ListNode(0)
#         prev = dummy

#         while head1 and head2:
#             if head1.val >= head2.val:
#                 prev.next = head2
#                 head2 = head2.next
#             else:
#                 prev.next = head1
#                 head1 = head1.next
#             prev = prev.next
            
#         if head1 is not None:
#             prev.next = head1
#         else:
#             prev.next = head2
            
#         return dummy.next


# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
#         if len(lists) > 0:
#             step = 1
#             while step < len(lists):
#                 for i in range(0,len(lists) - step,step*2):
#                     lists[i] = merge_2_lists(lists[i],lists[i+step])
#                 step *= 2
#             return lists[0]
#         return 



class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(min_heap,(lists[i].val,i,lists[i]))

        
        dummy = ListNode(0)
        prev = dummy

        while min_heap:
            value,index,node = heappop(min_heap)
            prev.next = node
            prev = prev.next

            if node.next:
                heappush(min_heap,(node.next.val,index,node.next))
        
        return dummy.next