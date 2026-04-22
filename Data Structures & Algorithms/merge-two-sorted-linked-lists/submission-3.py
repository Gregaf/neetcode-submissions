# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Non Optimal: O(n logn) time complexity, O(n) space complexity
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: 
        if list1 is None and list2 is None:
            return None
        
        l1 = list1
        l2 = list2

        res = ListNode()
        tail = res
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return res.next