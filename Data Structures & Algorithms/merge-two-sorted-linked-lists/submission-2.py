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

        arr = []

        l1 = list1
        while l1 is not None:
            arr.append(l1)
            l1 = l1.next
        
        l2 = list2
        while l2 is not None:
            arr.append(l2)
            l2 = l2.next
        
        arr.sort(key=lambda x:x.val)

        res = arr[0]
        head = res
        for i in range(0, len(arr), 1):
            res.next = arr[i + 1] if i + 1 < len(arr) else None
            res = res.next

        return head