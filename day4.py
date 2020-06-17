'''Question:
This problem was asked by Stripe.
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
'''
l = [3, 4, -1, 1, 2, 5, 6, 10]

# extracting the positive numbers out
k = [i for i in l if i > 0]
length = len(k)

flag = length+2
check = 0

# marking all the non-required numbers with flag
for i in range(length):
    if(k[i] > length):
        k[i] = flag


for i in range(length):
    if k[i] == flag:
        continue
    v = abs(k[i])
    k[v-1] *= -1
    print(k)

# checking for index of first positive number
for i in range(length):
    if k[i] > 0:
        print(i+1)
        check = 1
        break

if check == 0:
    print(length+1)
