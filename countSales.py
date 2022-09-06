file = open('inf_22_10_20_26.txt')
a = [] 
m = int(file.readline())  # Удаляем первую строку(общее количество купленных товаров)
summ = 0
maxi = 0
for i in file:
    x = int(i)
    if x <= 50:
        summ += x
    else:
        a.append(x)
a.sort()
for i in range(len(a)):
    if i < len(a)//2:
        summ += a[i] * 0.75
        maxi = round(a[i])
    else:
        s += a[i]
print(round(summ), maxi)