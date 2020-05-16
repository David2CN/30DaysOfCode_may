class Node:
    """
    Node implementation
    """
    def __init__(self, value = None, next = None):
        """
        constructor
        """
        assert type(value) == int, "Error!"
        self.value = value
        self.next = next
        

class Queue:
    """
    Implementation of Queue
    """
    def __init__(self):
        """
        constructor
        """
        self.head = None
    
    
    def enqueue(self, value):
        """
        appends/pushes a value to the end of the queue
        """
        assert type(value) == int, "Error!"
        value = Node(value = value)
        if not self.head:
            self.head = value
            return self.head
        else:
            curr = self.head
            while curr.next:
                curr = curr.next         
            curr.next = value
            
    
    def dequeue(self):
        """
        function to remove the element in front of the queue
        """
        assert self.head != None, "Error!"
        temp = self.head
        self.head = self.head.next
        return temp.value
                       
        
    def front(self):
        """
        function to return the node in front of the queue
        """
        if self.head == None:
            return None
        return self.head.value
    
    
    def count(self):
        """
        counts the number of elements in ths queue
        """
        if self.head == None:
            return 0
        temp = self.head
        count = 1
        while (temp.next != None):
            temp = temp.next
            count += 1
        return count
        
    def __repr__(self):
        """
        function to print the nodes in the queue
        """
        queue = ""
        node = self.head
        while node != None:
            queue += str(node.value) + "-->"
            node = node.next           
        return queue