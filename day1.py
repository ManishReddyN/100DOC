from random import seed, randint

seed(1)
l = [0] * 10000
for i in range(10000):
    l[i] = randint(0, 1000)
k = int(input())
flag = 0
for i in l:
    t = k - i
    if t in l:
        print("exists")
        flag = 1
        break
if flag == 0:
    print("doesn't exist")
