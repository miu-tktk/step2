#1 デバッグしてもらったときのコメントアウトの記録用
import itertools
from tqdm import tqdm
import cProfile

SCORES = {"a": 1, "b": 3, "c": 2, "d": 2, "e": 1, "f": 3, "g": 3, "h": 1, "i": 1, "j": 4, "k": 4, "l": 2, "m": 2, "n": 1, "o": 1, "p": 3, "q": 4, "r": 1, "s": 1, "t": 1, "u": 2, "v": 3, "w": 3, "x": 4, "y": 3, "z": 4}
ALPHABETS = "abcdefghijklmnopqrstuvwxyz"

test_file = "large.txt"
with open(test_file, 'r') as f:
    original_random_word_list = f.read().splitlines()
# original_random_word_list = ["aab"]
#create new dictionary
new_dictionary = []
with open('words.txt', 'r') as f:
        wordlist = f.read().splitlines()
# wordlist = ["ab", "abb"]
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
    # print(word)
    # print(score)
    new_dictionary.append({'original': word, 'count': count, 'score': score})#sort by score
new_dictionary.sort(key=lambda x: x['score'], reverse=True) 
# print(new_dictionary) #ここまではできてる

#create score and count in random_word list
random_word_list = []

for word in original_random_word_list:
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
  random_word_list.append({'count': count, 'score': score})
# print(random_word_list)
#compare the count and find anagram
# print(new_dictionary)
answer = []
for random_word in tqdm(random_word_list):
  for word in new_dictionary:
    # print(word)
    # print(random_word)
    if random_word['score'] < word['score']:#
      pass
    else:
      isanagram = True
      for char in ALPHABETS: 
        if random_word['count'][char] < word['count'][char]:
          isanagram = False
          # print(word)
          # print(random_word)
          # print(char)
          # print(word['count'])
          # print(random_word['count'])
          break
      if isanagram:
        answer.append(word['original'])
        break
      
output_file = 'large_answer.txt'
with open(output_file, 'w') as f:
    for ans in answer:
        f.write(f"{ans}\n")