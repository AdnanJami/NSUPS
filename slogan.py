x = int(input())
i = 0
dictionary = {}
while i < x:
    word = input()
    word1 = input()
    dictionary[word] = word1
    i += 1
y = int(input())
i = 0
while i < y:
    wrd = input()
    print(dictionary[wrd])
    y += 1
