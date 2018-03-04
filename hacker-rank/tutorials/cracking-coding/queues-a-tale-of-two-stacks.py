class MyQueue(object):
    def __init__(self):
        self.first = []  # newest on top
        self.second = [] # oldest on top
        
    def shiftStacks(self):
      if self.second == []:
        while self.first != []:
          self.second.append(self.first.pop())
        
    def isEmpty(self):
      return self.first == [] and self.second == []
    
    def peek(self):
      if self.isEmpty(): return None
      
      self.shiftStacks()
      return self.second[len(self.second) - 1]
        
    def put(self, value):
      self.first.append(value)
        
    def pop(self):
      if self.isEmpty(): return None
      
      self.shiftStacks()
      self.second.pop()
        

queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())
    
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()
        
