class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# head <-> tail
# head <-> 3 <-> 1 <-> 2 <-> tail

#head: prev: None
#      next: 3

#3: prev: head
#   next: 1

#1: prev: 3
#   next: 2

#2: prev: 1
#   next: tail

#tail: prev: 2
#      next: None

class Deque:
    #Initialize Deque
    def __init__(self):
        self.size = 0
        self.head = ListNode("head")
        self.tail = ListNode("tail")
        self.head.next = self.tail
        self.tail.prev = self.head


    # Return Type: Boolean
    # Description: Return True if the deque is empty, else False
    def isEmpty(self):
        return self.getSize() == 0

    # Return Type: int
    # Description: Return the number of items in the deque
    def getSize(self):
        return self.size

    # Return Type: None
    # Description: Insert item to the front of the deque
    def addFirst(self, item):
        # head <-> tail
        # head <-> 1 <-> tail
        # head <-> 2 <-> 1 <-> tail

        new_node = ListNode(item)
        prev_first = self.head.next
        #update head.next.prev
        self.head.next.prev = new_node
        #update head.next
        self.head.next = new_node
        #update new nodes next and prev
        new_node.prev = self.head
        new_node.next = prev_first
        self.size += 1

    # Return Type: None
    # Description: Insert item to the end of the deque
    def addLast(self, item):
        # head <-> tail
        # head <-> 1 <-> tail
        # head <-> 1 <-> 2 <-> tail

        new_node = ListNode(item)
        prev_last = self.tail.prev
        #update tail.prev.next
        self.tail.prev.next = new_node
        #update tail.prev
        self.tail.prev = new_node
        #update new nodes next and prev
        new_node.next = self.tail
        new_node.prev = prev_last
        self.size += 1

    # Return Type: Object
    # Description: Delete and return the item at the front of the deque
    def removeFirst(self):
        # head <-> 1 <-> 2 <-> tail
        # head <-> 2 <-> tail

        # head <-> 2 <-> tail

        # head <-> tail
        if self.isEmpty():
            print("trying to remove from empty list")
            return

        #2.prev = self.head
        #head.next = 2
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        self.size -= 1



    # Return Type: Object
    # #Description: Delete and return the item at the end of the deque
    def removeLast(self):
        # head <-> 1 <-> 2 <-> tail
        # head <-> 1 <-> tail

        # head <-> 1 <-> tail

        # head <-> tail
        if self.isEmpty():
            print("trying to remove from empty list")
            return


        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        self.size -= 1

    # Return Type: List
    # Description: construct a List holding all of the items in the deque from front to end and return it
    def asList(self):
        lst = []
        cur = self.head.next
        while(cur.next):
            lst.append(cur.val)
            cur = cur.next
        return lst




if __name__ == '__main__':
    #test cases
    dq = Deque()
    for i in range(1,6):
        dq.addFirst(i)
    for i in range(6,11):
        dq.addLast(i)

    # 5,4,3,2,1,6,7,8,9,10
    print(dq.asList())
    dq.removeFirst()
    print(dq.asList())
    #4,3,2,1,6,7,8,9,10
    dq.removeLast()
    print(dq.asList())
    #4,3,2,1,6,7,8,9
