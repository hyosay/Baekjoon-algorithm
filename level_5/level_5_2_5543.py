burger = []
drink = []
for i in range(0,3):
    burger.append(int(input()))
for j in range(0,2):
    drink.append(int(input()))
price = min(burger) + min(drink) - 50
print(price)