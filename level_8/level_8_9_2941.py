croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
croatia_c = input()
print(croatia_c)
for i in croatia:
    croatia_c = croatia_c.replace(i,'a')
print(list(croatia_c))
