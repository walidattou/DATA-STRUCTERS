class Node:
    def __init__(self,DATA):
        self.DATA = DATA
        self.next = None


class LinkedL:
    def __init__(self,head=None):
        self.head = head


    def Append(self,DATA):
        New_node = Node(DATA)
        if self.head is None:
            self.head = New_node
        else:
            current = self.head
            current.next = current
            while current.next:
                current = current.next
    
    def dis(self):
        curr = self.head
        if curr:
            while curr:
                print(curr.DATA)
                curr = curr.next

my = LinkedL()
my.Append(1)
my.Append(2)
my.Append(3)
my.dis()