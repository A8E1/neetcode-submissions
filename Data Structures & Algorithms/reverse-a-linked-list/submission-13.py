# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # initialize a prev, curr pointer
        prev, curr = None, head

        '''
        loop that
        1) ends when the iteration eaches the end of the linked lists
        '''
        while curr:
            # save the location of the next node before we redirect direction
            temp = curr.next

            # redirect current node (curr pointer) to point to previous node
            curr.next = prev

            # move the 2 pointer: prev & curr forward
            prev = curr
            curr = temp
        return prev



# class Solution:

    # Define a method named reverseList that takes the head of a linked list
    # and returns the new head after reversing the list.
    # def reverseList(self, head: ListNode) -> ListNode:

        # Create two pointers:
        # - prev starts as None (the reversed list is empty at first)
        # - curr starts at head (the node we are currently processing)
        # prev, curr = None, head

        # Keep looping as long as curr is not None (meaning we haven't hit the end)
        # while curr:

            # Save the next node before we break the link
            # (so we don’t lose the rest of the list after reversing the pointer)
            # temp = curr.next

            # Reverse the link: make the current node point backward to prev
            # curr.next = prev

            # Move prev forward to become the current node (growing the reversed part)
            # prev = curr

            # Move curr forward to the saved next node (continue through the original list)
            # curr = temp

        # When the loop ends, prev is the new head of the reversed list, so return it
        # return prev
