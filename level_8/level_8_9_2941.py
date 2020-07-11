'''croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
croatia_c = input()
print(croatia_c)
for i in croatia:
    croatia_c = croatia_c.replace(i,'a')
print(list(croatia_c))
'''

import re
sample = '이름 : 김파이, 연락처: 010-1234-5678, 주소: 부산 어딘가'
pattern = re.compile(r'[가-힣]{2,4}')
match = re.search(pattern, sample)

for i in range(1, 5):
    print(match.group())