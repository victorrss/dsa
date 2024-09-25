# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ks=[]
        # gather all the first nodes of each element in the list => Format: (val, index)
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(ks, (lists[i].val, i))
                lists[i] = lists[i].next

        root = ListNode()
        current = root
        while ks:
            val, i = heapq.heappop(ks) # returns min value
            current.next = ListNode(val)
            current = current.next
            if lists[i]:
                heapq.heappush(ks, (lists[i].val, i)) # add the next node of each list to it. it will keep the order because the lists are sorted
                lists[i] = lists[i].next
        
        return root.next

        # First bad version = O(L * n) => where L is the lists and n is the nodes.
        # if not len(lists):
        #     return None
        
        # allLists = list()
        # for i in range(len(lists)):
        #     current = lists[i]
        #     while current:
        #         heapq.heappush(allLists, current.val)
        #         current = current.next
        
        # if not len(allLists):
        #     return None
 
        # root = ListNode()
        # current = root
        # while allLists:
        #     next_val = heapq.heappop(allLists)
        #     current.next = ListNode(next_val)
        #     current = current.next
        
        # return root.next
        
