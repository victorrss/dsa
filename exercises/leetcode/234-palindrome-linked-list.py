# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        pointer = head
        while pointer != None:
            stack.append(pointer.val)
            pointer = pointer.next

        pointer = head
        while pointer != None:
            if pointer.val != stack.pop():
                return False
            pointer = pointer.next

        return True
