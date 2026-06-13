# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ''' use fast + slow pointers because the algorithm will help us determine
        # if there is a cycle in o(1) space complexity instead of o(n) space complexity
         o(n) will still be the time complexity
        '''
        # initialze pointer to reference the same object
        slow, fast = head, head

        # loop returns true if cycle exists, check if there's a next node (fast.next = Null) & is fast Null currently (fast)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow: # needs to be after increment because at first iteration, fast + slow are at the head
                return True

        # if the entire list has been traversed, and the if-condition
        # was not executed, then return false
        return False

'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Create two pointers that both start at the head of the linked list:
        # - slow will move 1 node at a time
        # - fast will move 2 nodes at a time
        slow, fast = head, head

        # Keep looping as long as fast can safely move forward:
        # - fast must not be None (end of list)
        # - fast.next must not be None (otherwise fast.next.next would crash)
        while fast and fast.next:

            # Move slow forward by 1 step
            slow = slow.next

            # Move fast forward by 2 steps
            fast = fast.next.next

            # If there is a cycle, fast will eventually "lap" slow and they will point
            # to the exact same node at some point inside the cycle
            if slow == fast:
                # Meeting means a cycle exists
                return True

        # If we exit the loop, fast hit None (end of list), so no cycle exists
        return False
'''
    
