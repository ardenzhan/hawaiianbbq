#RECURSIVE
def binarySearch(array, x, left = 0, right = None):
  if right is None: right = len(array) - 1

  if left > right: return False

  # to prevent overflow
  mid = left + ((right - left) / 2)

  if array[mid] is x: 
    return True
  elif x < array[mid]: 
    return binarySearch(array, x, left, mid - 1)
  else: 
    return binarySearch(array, x, mid + 1, right)

def binarySearchIterative(array, x):
  left = 0
  right = len(array) - 1

  while left <= right:
    mid = left + ((right - left) / 2)
    if array[mid] is x:
      return True
    elif x < array[mid]:
      right = mid - 1
    else: 
      left = mid + 1
      
  return False

test = [1, 23, 4, 5]
print binarySearch(test, 1)
print binarySearchIterative(test, 1)
print binarySearch(test, 8)
print binarySearchIterative(test, 8)