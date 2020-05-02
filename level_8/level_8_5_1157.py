'''word = input()
word.upper()
for i in word:
    count = 0
    for j in word:
        if i == j:
            count += 1
    print(count)'''
word = list(input().upper())
word_set = set(word)
for i in word_set:
    c = word.count(i)
idx = [i for i, x in enumerate(c) if x == max(c)]
if len(idx) > 1:print('?')
else: print(list(set(word_set))[c.index(max(c))])







