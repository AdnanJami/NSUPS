from sys import stdin
from re import split

dictionary = stdin.read()
text = dictionary.strip().lower()
words = set(split(r'[^a-z]', text))

for word in sorted(words):
    if word:
        print(word)
