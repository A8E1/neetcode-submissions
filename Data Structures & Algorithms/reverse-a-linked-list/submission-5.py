# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #return the new beginning of the list
        #given head pointer for curr list....
        #will iterate thru head -> .. -> .. -> .. 
        # im thinkin some sort of recursive step is necessary here...

        #we iterate thru to the last node
        #base case will be next == null
        #then recursive step unfolds setting next => node from func call above until top level next => null

      #iterative solution first:

        # prev, curr = None, head

        # while curr:
        #     nextNode = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nextNode
        # return prev

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead

