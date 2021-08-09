y= []
#y  لیست اعداد ورودی
p = []
# لیست مقسوم علیه ها
z =[]
counter = 0
while counter < 10:
    x = int(input())
    counter +=1
    y.append(x)

for num in range(1,11):
    for i in range(1,num):
        if (num % i!=0):
            p.append(num)

def maghsoom (e):
    k = 0
    for i in range (1, e + 1):     
        if e % i == 0:
            k += 1
    return (k)

for i in p:
    h = maghsoom (i)
    z.append (h)


print(y)
print(p)
print(z)
i = p.index(max(p))
print(y[i], end=' ')
print(max(p))
