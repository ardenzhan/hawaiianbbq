class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

  def insert(self, value):
    # recursively add value
    if value <= self.data:
      if self.left == None:
        self.left = Node(value)
      else: self.left.insert(value)
    elif value > self.data:
      if self.right == None:
        self.right = Node(value)
      else: self.right.insert(value)

  def contains(self, value):
    # recursively check if value exists in BST
    if value == self.data: return True
    elif value < self.data:
      if self.left == None: return False
      else: return self.left.contains(value)
    elif value > self.data:
      if self.right == None: return False
      else: return self.right.contains(value)
      
  def printInOrder(self):
    # InOrder Traversal - print left, root, then right

    # left subtree
    if self.left != None:
      self.left.printInOrder()

    # root
    print self.data

    # right subtree
    if self.right != None:
      self.right.printInOrder()


# cool!
tree = Node(5)
tree.insert(6)
tree.insert(7)
tree.insert(19)
tree.insert(-1)
tree.printInOrder()
print "tree contains 12?", tree.contains(12)
print "tree contains 7?", tree.contains(7)