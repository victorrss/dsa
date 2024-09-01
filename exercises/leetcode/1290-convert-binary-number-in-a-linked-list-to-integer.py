# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Approach of using bitwise shift left and OR operation
# i.e. [1 0 1] => the first is 1, so I will shift 1 left turning it 10 bin and doing OR with the next val 0, like 10 | 0, the result will be 10 bin = 2 decimal.
# after this it gets the next and shift 1 left again, it gets 100, and doing OR, like 100 | 1, it results in 101 bin or 5 decimal
# Time Complexity is O(n) and Space is O(1)
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        sum = head.val
        while head.next != None:
            sum = sum << 1 | head.next.val
            head = head.next
        return sum

# # Using the approach of the binary scale from the begining
# # i.e. [1 0 1]
# #    i*2+next 
# # Time Complexity is O(n) and Space is O(1)
# class Solution:
#     def getDecimalValue(self, head: ListNode) -> int:
#         sum = head.val
#         while head.next != None:
#             sum = sum*2 + head.next.val
#             head = head.next
#         return sum

# # Using the approach of the binary scale from the last
# # i.e. [1 0 1]
# #       4 2 1 => to the power of
# # so i can use a stack to start using the last
# # But the Time Complexity is O(n*2)
# # class Solution:
# #     def getDecimalValue(self, head: ListNode) -> int:
# #         stack = []
#         while head:
#             stack.append(head.val)
#             head = head.next
#         sum = 0
        
#         for i in range(len(stack)):
#             if stack.pop() == 1:
#                 sum += pow(2, i)
#         return sum
