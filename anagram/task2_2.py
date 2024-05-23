#2
import time

start = time.time()

SCORES = {"a": 1, "b": 3, "c": 2, "d": 2, "e": 1, "f": 3, "g": 3, "h": 1, "i": 1, "j": 4, "k": 4, "l": 2, "m": 2, "n": 1, "o": 1, "p": 3, "q": 4, "r": 1, "s": 1, "t": 1, "u": 2, "v": 3, "w": 3, "x": 4, "y": 3, "z": 4}
ALPHABETS = "abcdefghijklmnopqrstuvwxyz"

test_file = "large.txt"
with open(test_file, 'r') as f:
    original_random_word_list = f.read().splitlines()

#create new dictionary
new_dictionary = []
with open('words.txt', 'r') as f:
        wordlist = f.read().splitlines()

for word in wordlist:
    score = 0
    count = {char: 0 for char in ALPHABETS}
    #score
    for char in word:
      score += SCORES[char]
    #count
    for char in word:
      if char in count:
        count[char] += 1
      else:
        count[char] = 1
    
    new_dictionary.append({'original': word, 'count': count, 'score': score})#sort by score
new_dictionary.sort(key=lambda x: x['score'], reverse=True) 


#create score and count in random_word list
random_word_list = []

for word in original_random_word_list:
  count = {char: 0 for char in ALPHABETS}
  #count
  for char in word:
    if char in count:
      count[char] += 1
    else:
      count[char] = 1

  random_word_list.append({'count':count})

#compare the count and find anagram

answer = []
for random_word in random_word_list:
  for word in new_dictionary:
      isanagram = True
      for char in ALPHABETS: 
        if random_word['count'][char] < word['count'][char]:
          isanagram = False
          break
      if isanagram:
        answer.append(word['original'])
        break
      
output_file = 'large_ans.txt'
with open(output_file, 'w') as f:
    for ans in answer:
        f.write(f"{ans}\n")

end = time.time()  
time_diff = end - start
print(time_diff)