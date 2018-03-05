def get_dict(text):
  text_dict = {}
  for word in text:
    if word not in text_dict: 
      text_dict[word] = 1
    else: 
      text_dict[word] += 1
  return text_dict

def compare_dict(mag, ran):
  for word in ran:
    if word not in mag: return False
    else: 
      mag[word] -= ran[word]
      if mag[word] < 0: return False
  return True

def ransom_note(magazine, ransom):
  magazine_dict = get_dict(magazine)
  ransom_dict = get_dict(ransom)
  return compare_dict(magazine_dict, ransom_dict)
    

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
    
