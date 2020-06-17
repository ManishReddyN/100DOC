''' Question
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.'''

l = [10, 15, 3, 7]
k = 17
s = set(l)  # converting list l into a set and storing it in s
flag = 0
for i in s:
    if (k-i) in s:
        print("pair exists")
        flag = 1
        break
if flag == 0:
    print("pair doesn't exist")
