def quicksort(array, left = None, right = None):
  if left is None: left = 0
  if right is None: right = len(array) - 1

  if (left >= right): return

  pivot = array[(left + right) / 2]
  index = partition(array, left, right, pivot)

  # quicksort left side
  quicksort(array, left, index - 1)

  # quicksort right side
  quicksort(array, index, right)
    
def partition(array, left, right, pivot):
  # swap all elements where smaller than pivot elements are to left
  # bigger than pivot elements to the right
  # return partition point, which is where left will be

  while left <= right:

    # keep moving left and right pointers toward pivot until find values to swap
    while array[left] < pivot:
      left += 1

    while array[right] > pivot:
      right -= 1

    if left <= right:
      # swap
      array[left], array[right] = array[right], array[left]
      left += 1
      right -= 1
  
  return left

test = [9,2,6,4,3,5,1]
print test
quicksort(test)
print test