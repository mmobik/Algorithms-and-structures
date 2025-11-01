class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            value =  self.current.value
            self.current = self.current.next
            return value

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__length = 0
    
    def append(self, value, position = None):
        node = ListNode(value)

        if position is None:
            if self.head is None:
                self.head = node
                self.tail = node
            else:
                self.tail.next = node
                self.tail = node
            self.__length += 1
        
        else:
             if position < 0 or position > self.__length:
                 raise ValueError("Index out of range")

             if position == 0:
                 node.next = self.head
                 self.head = node
                 if self.__length == 0:
                     self.tail = node
                 self.__length += 1

             elif position == self.__length:
                 self.tail.next = node
                 self.tail = node
                 self.__length += 1
            
             else:
                 current = self.head
                 for pos in range(position - 1):
                     current = current.next
                 node.next = current.next
                 current.next = node
                 self.__length += 1

    
    def __iter__(self):
        return LinkedListIterator(self.head)
    
    @property
    def len(self):
        return self.__length
    

    def delete(self, value):

        if self.head is None:
            raise ValueError("Linked list is empty")

        elif self.head.value == value:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            
            self.__length -= 1
            return True
        
        current = self.head
        while current.next:
            if current.next.value == value:
                if current.next == self.tail:
                    self.tail = current
                else:        
                    current.next = current.next.next
                    self.__length -= 1
                    return True
            current = current.next
        
        return False
