from itertools import permutations

letters = "ABCDEFGHIK"
word_length = 7

unique_words = set()
for perm in permutations(letters, word_length):
    unique_words.add("".join(perm))

print("Total number of unique words:", len(unique_words))
