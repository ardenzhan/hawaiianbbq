# return location and length of longest repeating substring

test = "101111010"
test2 = "ABAAAACcCAAAc"

def find(input):
  largestIndex = 0
  largestCount = 0

  currentIndex = 0
  currentCount = 0
  for i in range(len(input)):
    if input[i] is input[currentIndex]:
      currentCount += 1
    
    else:
      if currentCount > largestCount:
        largestCount = currentCount
        largestIndex = currentIndex
      
      currentIndex = i
      currentCount = 1
  
  print largestIndex, largestCount

find(test)
find(test2)