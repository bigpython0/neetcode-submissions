# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = iterator
        curr1 = 0
        curr2 = 0
        iterator = None

        while list1 and list2:
            curr1 = list1
            curr2 = list2

            if curr1.val <= curr2.val:
                iterator.next = curr1
                curr1 = curr1.next
            else:
                iterator.next = curr2
                curr2 = curr2.next
            iterator = iterator.next
        if not list1 and not list2:
            return head
        elif not list2:
            iterator.next = curr1
        elif not list1:
            iterator.next = curr2
            
        