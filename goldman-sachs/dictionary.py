'''
str, dictionary
{"word": ["aa", "he", "llo", "olleh", "olehl"]}
find longest valid word in dictionary, using letters from str
'''

string = 'hello'
dictionary = {'words': ["aa", "he", "llo", "oolleh", "olehl"]}

def getMap(string):
  # key: letter, value: count of letter
  letter_map = {}
  for char in string: 
    if char in letter_map:
      letter_map[char] += 1
    else: letter_map[char] = 1
  return letter_map

def checkMap(string, word):
  strMap = getMap(string)
  dictMap = getMap(word)

  for key in dictMap:
    if key not in strMap: return False
    if dictMap[key] > strMap[key]: return False
  
  return True

longestWord = ''
for word in dictionary['words']:
  if checkMap(string, word) and len(word) > len(longestWord):
    longestWord = word
print longestWord

# print getMap('hello')


