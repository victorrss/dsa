class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # initialize the pointer for the last 
        while head:
            current = head # pointer for this iteration
            head = head.next # change the pointer of this loop
            current.next = prev # change the next to the previous pointer
            prev = current # updates the prev pointer to be used in the next iteration
           
        return prev
