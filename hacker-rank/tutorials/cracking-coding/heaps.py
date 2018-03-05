class MinHeap:
  def __init__(self):
    self.size = 0
    self.items = []

  def getLeftChildIndex(self, parentIndex): return 2 * parentIndex + 1
  def getRightChildIndex(self, parentIndex): return 2 * parentIndex + 2
  def getParentIndex(self, childIndex): return (childIndex - 1) / 2

  def hasLeftChild(self, index): return self.getLeftChildIndex(index) < self.size
  def hasRightChild(self, index): return self.getRightChildIndex(index) < self.size
  def hasParent(self, index): return self.getParentIndex(index) >= 0

  def leftChild(self, index): return self.items[self.getLeftChildIndex(index)]
  def rightChild(self, index): return self.items[self.getRightChildIndex(index)]
  def parent(self, index): return self.items[self.getParentIndex(index)]

  def swap(self, indexOne, indexTwo):
    self.items[indexOne], self.items[indexTwo] = self.items[indexTwo], self.items[indexOne]
  
  def peek(self):
    # return root, which will be minimum element of heap
    if self.size is 0: return None
    return self.items[0]

  def poll(self):
    """ 
    retrieve (pop) root element of heap
    swap last added element to the root, then Heapify down (reorder back down with bubble)
    """

    if self.size is 0: return None
    item = self.items[0]
    self.items[0] = self.items[self.size - 1]
    self.size -= 1
    self.heapifyDown()
    return item

  def add(self, item):
    """
    add (push) item to end of heap (array)
    Heapify up until in order
    """
    self.items.append(item)
    self.size += 1
    self.heapifyUp()

  def heapifyDown(self):
    # start with root, keep swapping down while children are smaller (out of order)
    index = 0

    # only needs to check left child, because no right if no left
    while self.hasLeftChild(index):

      # set smallerChildIndex to smaller of left or right child
      smallerChildIndex = self.getLeftChildIndex(index)
      if self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index):
        smallerChildIndex = self.getRightChildIndex(index)
      
      if self.items[index] < self.items[smallerChildIndex]: break
      else: self.swap(index, smallerChildIndex)
      
      index = smallerChildIndex

  def heapifyUp(self):
    # start with last added element then walk up while there's a larger parent (out of order)
    index = self.size - 1
    while self.hasParent(index) and self.parent(index) > self.items[index]:
      self.swap(self.getParentIndex(index), index)
      index = self.getParentIndex(index)


test = MinHeap()
test.add(4)
test.add(5)
test.add(10)
test.add(1)
print test.items
print 'Polled: {}'.format(test.poll())
print test.items