word = input().upper()
word_set = set(word)
c = []
for i in word_set:
    c.append(word.count(i))
idx = [i for i, x in enumerate(c) if x == max(c)]
if len(idx) > 1:
    print('?')
else: print(list(set(word_set))[c.index(max(c))])


#2
s = input().upper()
m = 0
for i in set(s):
    y = s.count(i)
    if m < y:
        m, c = y, i
    elif m == y:
        c = '?'
print(c)
