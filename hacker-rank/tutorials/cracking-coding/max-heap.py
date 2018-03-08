class MaxHeap:
  def __init__(self):
    self.items = []

  def __repr__(self):
    return 'Heap: {}'.format(self.items)

  def getLeftChildIndex(self, parentIndex): return 2 * parentIndex + 1
  def getRightChildIndex(self, parentIndex): return 2 * parentIndex + 2
  def getParentIndex(self, childIndex): return (childIndex - 1) / 2

  def hasLeftChild(self, index): return self.getLeftChildIndex(index) < len(self.items)
  def hasRightChild(self, index): return self.getRightChildIndex(index) < len(self.items)
  def hasParent(self, index): return self.getParentIndex(index) >= 0

  def leftChild(self, index): return self.items[self.getLeftChildIndex(index)]
  def rightChild(self, index): return self.items[self.getRightChildIndex(index)]
  def parent(self, index): return self.items[self.getParentIndex(index)]

  def swap(self, indexA, indexB):
    self.items[indexA], self.items[indexB] = self.items[indexB], self.items[indexA]
  
  def peek(self):
    # return root, which will be max element of heap
    if len(self.items) is 0: return None
    return self.items[0]

  def poll(self):
    """ 
    retrieve (pop) root (max) element of heap
    move last added element to the root, then Heapify down (reorder back down with bubble)
    """
    if len(self.items) is 0: return None

    item = self.items[0]
    self.items[0] = self.items.pop()
    self.heapifyDown()
    return item

  def add(self, item):
    """
    add (push) item to end of heap (array)
    Heapify up until in order
    """
    self.items.append(item)
    self.heapifyUp()

  def heapifyDown(self):
    # start with root element, keep swapping element down while children are larger (out of order)
    index = 0

    # only needs to check left child, because no right if no left
    while self.hasLeftChild(index):

      # set largerChildIndex to larger of left or right child
      largerChildIndex = self.getLeftChildIndex(index)
      if self.hasRightChild(index) and self.rightChild(index) > self.leftChild(index):
        largerChildIndex = self.getRightChildIndex(index)
      
      if self.items[index] > self.items[largerChildIndex]: break
      else: self.swap(index, largerChildIndex)
      
      index = largerChildIndex

  def heapifyUp(self):
    # start with last added element then walk up while there's a smaller parent (out of order)
    index = len(self.items) - 1
    while self.hasParent(index) and self.parent(index) < self.items[index]:
      self.swap(self.getParentIndex(index), index)
      index = self.getParentIndex(index)


test = MaxHeap()
test.add(4)
print test
test.add(5)
print test
test.add(10)
print test
test.add(1)
print test
print 'Polled: {}'.format(test.poll())
print test