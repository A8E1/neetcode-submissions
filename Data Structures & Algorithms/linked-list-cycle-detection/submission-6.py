# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #store each node visited in set
        #membership check for each new node
        #return True if seen b4
        

        # seen = set()

        # cur = head

        # while cur:
        #     if cur in seen:
        #         return True
            
        #     seen.add(cur)
        #     cur = cur.next
        # return False


        # #got it

        fast = head
        slow = head

        while fast and fast.next:

            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        
        return False

        