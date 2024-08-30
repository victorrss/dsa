class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertHead(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    
    def insertEnd(self, data):
        newNode = Node(data)
        
        if self.head == None:
            self.head = newNode
            return
            
        pointer = self.head
        while pointer.next != None:
            pointer = pointer.next
        pointer.next = newNode
    
    def insertAfter(self, data, pos):       
        newNode = Node(data)
        # When trying to add in an invalid position (negative side)
        if pos < 1:
            self.insertHead(data)
            return
        
        prev = self.head
        for _ in range(pos-1):
            # When trying to add in an invalid position (positive side)
            if prev.next == None:
                self.insertEnd(data)
                return
            prev = prev.next
        newNode.next = prev.next
        prev.next = newNode
        
    def removeBegin(self):
        if self.head:
            self.head = self.head.next
            
    def removeEnd(self):
        if not self.head:
            return
        elif self.head.next == None:
            self.head = None
            return
        
        prev = self.head
        while prev.next.next != None:
            prev = prev.next
        prev.next = None
    
    def search(self, value):
        if not self.head:
            return None
        
        prev = self.head
        i = 1
        while prev != None:
            if prev.data == value:
                return i
            i += 1
            prev = prev.next
            
    def reverse(self):
        # Initialize pointers
        prev = None
        curr = self.head
        
        # Traverse all the nodes of Linked List
        while curr:
            # Store next
            next_node = curr.next
            # Reverse current node's next pointer
            curr.next = prev 
            # Move pointers one position ahead
            prev = curr
            curr = next_node
        # Return the head of reversed linked list
        self.head = prev
        
    def print(self):
        if self.head == None:
            print("Empty list")
            return
        
        list = []    
        
        pointer = self.head
        while pointer != None:
            list.append(str(pointer.data))
            pointer = pointer.next
        
        print(" -> ".join(list))

def main():
    list = LinkedList()
    print('List created')
    list.print() # Empty list
    
    print('insert 2 to head')
    list.insertHead(2)
    list.print() # 2
    
    print('insert 3 to end')
    list.insertEnd(3)
    list.print() # 2 -> 3
    
    print('insert 1 to head')
    list.insertHead(1) 
    list.print() # 1 -> 2 -> 3
    
    print('insert 10 to position 2 (insert 10 after the second element)')
    list.insertAfter(10, 2) 
    list.print() # 1 -> 2 -> 10 -> 3
    
    print('Reverse the list')
    list.reverse()
    list.print()
    
    print('Remove from the begining')
    list.removeBegin() 
    list.print() # 2 -> 10 -> 3
    
    print('Remove from the end')
    list.removeEnd() 
    list.print() # 2 -> 10
    
    print('Search 10 in the list, returns the position.')
    print(list.search(10)) # 2
    
    print('Remove from the end')
    list.removeEnd() 
    list.print() # 2

    print('Remove from the end')
    list.removeEnd() 
    list.print() # Empty list

if __name__ == '__main__':
    main()
