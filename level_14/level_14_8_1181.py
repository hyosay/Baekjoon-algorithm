N = int(input())
arp = []
larp = []
c = []
for i in range(0, N):
    arp.append(input())
    larp.append(len(arp[i]))
    c.append([arp[i], larp[i]])

c = sorted(c, key= lambda x: (x[1],x[0]))
c = set()
print(c)