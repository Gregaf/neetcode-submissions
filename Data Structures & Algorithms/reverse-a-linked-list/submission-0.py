# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        curr = head
        prev = None

        # curr = 
        # prev = curr.next

        while curr:
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next
        
        return prev
            
            

        # [0,1,2,3]
        # [1,0]
        