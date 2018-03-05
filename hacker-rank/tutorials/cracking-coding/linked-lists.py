# https://www.hackerrank.com/topics/linked-lists

class Node:
  def __init__(self, data = None, next_node = None):
    self.data = data
    self.next = next_node

class LinkedList:
  def __init__(self):
    self.head = None
  
  def append(self, data):
    if self.head is None: 
      self.head = Node(data)
      return

    current = self.head
    while current.next is not None:
      current = current.next
    current.next = Node(data)

  def prepend(self, data):
    newHead = Node(data)
    newHead.next = self.head
    self.head = newHead

  def deleteValue(self, data):
    if self.head is None: 
      return
    if self.head.data is data:
      self.head = self.head.next
      return

    current = self.head
    while current.next is not None:
      if current.next.data is data:
        current.next = current.next.next #skip the next value
        return
      current = current.next

  def printList(self):
    current = self.head
    while current is not None:
      print current.data,
      current = current.next
    print

test = LinkedList()
test.append(4)
test.append(5)
test.append(6)
test.prepend(1)
test.printList()
test.deleteValue(4)
test.printList()