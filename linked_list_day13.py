class  Node:
    def  __init__(self, value = None, next=None):
        """
        constructor
        """
        if value != None:
            assert type(value) == int, "Error!"
        if next != None:
            assert type(next) == Node, "Error!"
        self.value =  value
        self.next  =  next
    
    def __repr__(self):
        """
        function to print nodes
        """
        nodes = ""
        node = self
        while node:
            if node.value != None:
                nodes += str(node.value)+ "->"
            node = node.next
        return nodes
                  
def append(head, value):
    """
    function to add node to the end
    """
    assert type(head) == Node and type(value) == int, "Error!"
    if not head:
        head = Node(value = value)
        return head
    value = Node(value)
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = value

def get_last_node(head):
    """
    function to get last node
    """
    assert type(head) == Node, "Error!"
    temp = head
    while(temp.next is not None):
        temp = temp.next
    return temp  

def pop(head):
    """
    function to remove the last element from the nodes
    """
    assert type(head) == Node, "Error!"
    curr = head
    key = get_last_node(head)
    prev = None
    while curr != key:
        prev = curr
        curr = curr.next
    if prev is None:
        head = curr.next
    elif curr:
        prev.next = curr.next
        curr = None
        
head = Node(9)
append(head, 9)
append(head, 11)
append(head, 45)
append(head, 9)

pop(head)
pop(head)
pop(head)
pop(head)

append(head, 13)
print(head)        
        