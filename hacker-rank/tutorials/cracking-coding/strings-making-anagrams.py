def get_freq(string):
  freq = {}
  for char in string:
    if char not in freq:
      freq[char] = 1
    else:
      freq[char] += 1
  return freq
  
  
def get_delta_freq(freq1, freq2):
  delta = {}
  
  for key in freq1:
    delta[key] = freq1[key]
    
  for key in freq2:
    if key not in delta:
      delta[key] = freq2[key]
    else: 
      delta[key] = abs(freq2[key] - freq1[key])

  return delta


def number_needed(a, b):
  freq_a = get_freq(a)
  freq_b = get_freq(b)
  difference = get_delta_freq(freq_a, freq_b)
  return sum(difference.values())


a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)

# sample input:
# cde
# abc

# sample output:
# 4