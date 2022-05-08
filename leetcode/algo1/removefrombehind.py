# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = head
        pos = 0
        size = 1
        while ptr and ptr.next:
            ptr = ptr.next
            size +=1
        ptr = head
        if size == 1:
            head = None
        elif size == n:
            head = head.next
        else:
            while ptr and ptr.next:
                if pos == size-n-1:
                    if ptr.next.next:
                        ptr.next = ptr.next.next
                    else:
                        ptr.next = None        
                pos +=1
                ptr  = ptr.next
        return head