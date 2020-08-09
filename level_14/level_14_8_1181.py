N = int(input())
arp = []

for i in range(0, N):
    arp.append(input())
arp = list(set(arp))

list_arp = []
for j in arp:
    list_arp.append((len(j), j))
print(list_arp)
list_arp.sort()
for i in range(len(list_arp)):
    print(list_arp[i][1])
