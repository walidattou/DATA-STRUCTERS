import math

class Node:
    def __init__(self,DATA):
        self.DATA = DATA
        self.next = None

class Linked_L:

    def __init__(self,head = None):
        self.head = head
        self.counter = 0
    
    def append(self,DATA):
        New_node = Node(DATA)
        if self.head is None :
            self.head = New_node
            self.counter += 1
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
                self.counter += 1
            curr.next = New_node

    
    def dis(self):
        curr = self.head
        while curr:
            print(curr.DATA)
            curr = curr.next


    def disH(self):
        curr = self.head
        half_counter = 0
        while curr:
            half_counter+=1
            if half_counter == math.floor(self.counter/2):
                print(curr.DATA)
            curr = curr.next
 

    def Remove_by_index(self, index):
            curr = self.head
            prev = None
            counter = 0
            
            while curr:
                if counter == index:
                    if prev:  
                        prev.next = curr.next
                    
                prev = curr
                curr = curr.next
                counter += 1



L = Linked_L()

L.append(1)
L.append(2)
L.append(3)
L.append(4)
L.append(5)
L.dis()
print('####################################')
L.Remove_by_index(2)
L.dis()