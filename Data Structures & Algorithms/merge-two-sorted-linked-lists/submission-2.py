# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy node + node pointer 
        dummy = node = ListNode()
        
        # loop that traverses each node one-by-one & compares. Once the loop ends, 
        # it means one of the list has reached the end, therefore we need to just append the rest of the remaining list
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        
        # loop exits meaning that at least one of the lists are empty so append the rest of remaining linked list 
        node.next = list1 or list2

        return dummy.next

    '''
    # Define a class named Solution (this is the format LeetCode expects).
# class Solution:
    # def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

        """ Create a 'dummy' starter node (a fake head) so we don't have to handle
        the head of the merged list as a special case.
        Also create a pointer named node that will always point to the LAST node
        """ in the merged list that we've built so far.
        # dummy = node = ListNode()

        # Keep looping while BOTH lists still have nodes left to compare.
        # while list1 and list2:

            # Compare the current values at the heads of list1 and list2.
            # if list1.val < list2.val:

                """ Attach the current node from list1 to the end of our merged list.
                (We are not creating a new node; we are reusing the existing node.)
                """
                # node.next = list1

                # Move list1 forward to its next node (because we just used its current one).
                # list1 = list1.next

            # Otherwise, list2's head is smaller (or equal), so it should come next.
            # else:

                # Attach the current node from list2 to the end of our merged list.
                # node.next = list2

                # Move list2 forward to its next node (because we just used its current one).
                # list2 = list2.next

            # Move node forward to the node we just attached,
            # so node again points to the LAST node in the merged list.
            # node = node.next

        # At this point, one of the lists is empty.
        # The other list might still have nodes left, and since it's already sorted,
        # we can attach ALL remaining nodes directly to the end of the merged list.
        # (Only one of list1 or list2 is non-empty here.)
        # node.next = list1 or list2

        # dummy is a "fake" head, so the real head of the merged list is dummy.next.
        # Return dummy.next as the answer.
        # return dummy.next

    '''