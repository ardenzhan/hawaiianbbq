class Player:
    def __init__(self, name, score):
      self.name = name
      self.score = score
        
    def __repr__(self):
      return 'Name: {}, Score: {}'.format(self.name, self.score)
        
    def comparator(a, b):
      if a.score == b.score:
        return (a.name > b.name) - (a.name < b.name)
      
      return b.score - a.score

p = Player("Arden", 5)
print p