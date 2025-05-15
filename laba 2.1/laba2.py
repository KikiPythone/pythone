import itertools
count = 0
slovo = "НАСТЯ"
for a in itertools.product(slovo, repeat = 6):
    b = ''.join(a)
    if b.count("А") <= 1 and b.count("Я") <= 1:
        count+= 1
print(count)  




x = 16**18 * 4**10 - 46 - 16
s =''
while x!= 0:
    s += str(x % 4)
    x //= 4
s = s[::-1]
print(s.count("3"))




def F(n): 
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i + n // i
    return 0
k = 0
for i in range(452021 + 1, 10000000000000):
    if F(i) % 7 == 3:
        print(i, F(i))
        k += 1
    if k == 5: 
        break