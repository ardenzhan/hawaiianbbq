class Stack:
  
  class Node:
    def __init__(self, data):
      self.data = data
      self.next = None
      
  def __init__(self):
    self.top = None
    
  def isEmpty(self):
    return self.top == None

  def peek(self):
    return self.top.data
  
  def push(self, data):
    newNode = self.Node(data)
    newNode.next = self.top
    self.top = newNode

  def pop(self):
    data = self.top.data
    self.top = self.top.next
    return data

  # USING LIST
  # def __init__(self):
  #   self.items = []
  # def isEmpty(self):
  #   return self.items == []
  # def push(self, item):
  #   self.items.append(item)
  # def pop(self):
  #   return self.items.pop()
  # def peek(self):
  #   return self.items[len(self.items)-1]
  # def size(self):
  #   return len(self.items)

def getOpen(close):
  if close == '}': return '{'
  elif close == ')': return '('
  elif close == ']': return '['
  
def is_matched(expression):
  stack = Stack()
  for bracket in expression:
    if bracket in ['}', ')', ']']:
      if stack.isEmpty(): return False
      if stack.peek() == getOpen(bracket): stack.pop()
    else: stack.push(bracket)
      
  return stack.isEmpty()


# TESTING
t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"