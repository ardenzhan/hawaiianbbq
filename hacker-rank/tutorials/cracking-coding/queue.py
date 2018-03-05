class Queue:

  class Node:
    def __init__(self, data = None):
      self.data = data
      self.next = None
  
  def __init__(self):
    self.head = None # remove from head
    self.tail = None # add to tail

  def isEmpty(self):
    return self.head is None
  
  def peek(self):
    if self.head is None: return None
    return self.head.data

  def add(self, data):
    node = self.Node(data)
    if self.tail is not None:
      self.tail.next = node
    self.tail = node

    if self.head is None:
      self.head = node
    
    
  def remove(self):
    data = self.head.data
    self.head = self.head.next #removes head
    
    if self.head is None:
      self.tail = None
    
    return data

  def printQueue(self):
    current = self.head
    while current is not None:
      print current.data,
      current = current.next
    print


test = Queue()
test.add(5)
test.add(6)
test.add(1)
test.printQueue()
test.remove()
test.printQueue()