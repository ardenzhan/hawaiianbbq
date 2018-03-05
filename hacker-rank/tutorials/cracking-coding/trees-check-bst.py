""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkRange(root, min, max): #inclusive range
  if root == None: 
    return True
  
  if root.data < min or root.data > max: 
    return False
  
  return checkRange(root.left, min, root.data - 1) and checkRange(root.right, root.data + 1, max)

def checkBST(root):
  return checkRange(root, 0, 10**4)
  # could also be from (-infinity, +infinity) for min, max