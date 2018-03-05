def mergesort(array, temp = [], left = None, right = None):
  # left start, right end
  if left is None: left = 0
  if right is None: right = len(array) - 1

  if left >= right: return

  middle = (left + right) / 2

  # mergesort left half
  mergesort(array, temp, left, middle)

  # mergesort right half
  mergesort(array, temp, middle + 1, right)

  mergeHalves(array, temp, left, right)

def mergeHalves(array, temp, leftStart, rightEnd):
  leftEnd = (leftStart + rightEnd) / 2
  rightStart = leftEnd + 1
  size = rightEnd - leftStart + 1

  left = leftStart
  right = rightStart
  index = leftStart

  # copy over smaller elements of both halves
  while left <= leftEnd and right <= rightEnd:
    # print array, right, rightEnd

    if array[left] <= array[right]:
      if index >= len(temp): temp.append(array[left])
      else: temp[index] = array[left]
      left += 1
    else:
      if index >= len(temp): temp.append(array[right])
      else: temp[index] = array[right]
      right += 1

    index += 1

  # copy remainding elements once either left/right half is done
  # array[a:a+2] means copy over starting at a, 2 elements

  temp[index:index+(leftEnd-left+1)] = array[left:left+(leftEnd-left+1)]
  temp[index:index+(rightEnd-right+1)] = array[right:right+(rightEnd-right+1)]

  # copy temp to array
  array[leftStart:leftStart+size] = temp[leftStart:leftStart+size]


test = [10, 5, 2, 7, 4, 3]
mergesort(test)
print test