# Load and sort the dictionary
new_dictionary = []
with open('words.txt', 'r') as f:
    wordlist = f.read().splitlines()

# Create a list of tuples with sorted word and original word
for word in wordlist:
    changed = ''.join(sorted(word))
    new_dictionary.append((changed, word))

# Sort the list of tuples by the sorted word
new_dictionary.sort(key=lambda x: x[0])

# Function to find anagrams using binary search
def find_anagram(random_word):
    sorted_random_word = ''.join(sorted(random_word))
    
    # Binary search to find the position of the sorted random word
    left, right = 0, len(new_dictionary) - 1
    found = False
    while left <= right:
        mid = (left + right) // 2
        if new_dictionary[mid][0] == sorted_random_word:
            found = True
            break
        elif new_dictionary[mid][0] < sorted_random_word:
            left = mid + 1
        else:
            right = mid - 1
    
    # If the word is not found
    if not found:
        return "can't find anagram"
    
    # Collect all anagrams
    anagrams = [new_dictionary[mid][1]] #1:original word
    
    # Check left side of mid
    i = mid - 1
    while i >= 0 and new_dictionary[i][0] == sorted_random_word:
        anagrams.append(new_dictionary[i][1])
        i -= 1
    
    # Check right side of mid
    i = mid + 1
    while i < len(new_dictionary) and new_dictionary[i][0] == sorted_random_word:
        anagrams.append(new_dictionary[i][1])
        i += 1
    
    return anagrams

# Test case
random_word = "listen"
# random_word = "l isten"
# random_word = "あ"
print(find_anagram(random_word))
