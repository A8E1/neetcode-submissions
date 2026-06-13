# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #iterative solution:
            # we need to traverse LL, GOAL: point each node backwards
                # need: 2 pointers. one tracking the prev node, one iterating thru
                # the last iterating node => will be the head at that point


        prev, curr = None, head

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
            
        return prev

