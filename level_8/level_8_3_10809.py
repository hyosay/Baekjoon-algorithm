alphabet = 'abcdefghijklmnopqrstuvwxyz'
word_list = []
word_num = []
word = str(input())

for i in word:
    word_list.append(i)
for character in alphabet:
    for j in range(len(word_list)):
        if character == word_list[j]:
            word_num.append(j)
            break
        elif j < len(word_list) - 1:
            continue
        else:
            word_num.append(-1)
for i in word_num:
    print(i,end = ' ')
