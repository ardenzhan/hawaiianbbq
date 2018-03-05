n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

def bubbleSort(array):
  swap_count = 0
  isSorted = False
  lastUnsorted = n - 1
  while not isSorted:
    isSorted = True
    for i in range(lastUnsorted):
      if array[i] > array[i+1]:
        temp = array[i]
        array[i] = array[i+1]
        array[i+1] = temp
        swap_count += 1
        isSorted = False
        
    lastUnsorted -= 1
    
  print "Array is sorted in {} swaps.".format(swap_count)
  print "First Element: {}".format(array[0])
  print "Last Element: {}".format(array[n-1])
  
bubbleSort(a)
  

'''
for (int i = 0; i < n; i++) {
    
    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
        }
    }
    
}
'''