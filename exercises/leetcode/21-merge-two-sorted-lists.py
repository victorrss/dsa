# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        cur = ans
        while list1 or list2:
            if list1 and list2:
                if list1.val > list2.val:
                    cur.next = ListNode(list2.val)
                    list2 = list2.next
                elif list1.val < list2.val:
                    cur.next = ListNode(list1.val)
                    list1 = list1.next
                else:
                    cur.next = ListNode(list1.val)
                    cur = cur.next
                    cur.next = ListNode(list2.val)
                    list1 = list1.next
                    list2 = list2.next
            elif list1:
                cur.next = ListNode(list1.val)
                list1 = list1.next
            else:
                cur.next = ListNode(list2.val)
                list2 = list2.next
            cur = cur.next
            
        return ans.next
# Time O(m+n)
# Space O(1)
