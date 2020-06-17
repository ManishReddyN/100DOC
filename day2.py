'''Question:
This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
'''

a = [1, 2, 3, 4, 5]
length = len(a)
l = [0]*length
r = [0]*length
l[0] = 1  # since there is no element to the left of the first element we keep it's left product as 1
for i in range(1, length):
    l[i] = l[i-1]*a[i-1]
print(l)
'''Ex: take i=1 the left product at i=1 is product of all elements
to the left of it. Since we have the left product of the
previous element already stored in the list l we multiply
it with the element at i-1.'''

# since there is no element to the right of the last element.
r[length-1] = 1
for i in reversed(range(length-1)):
    r[i] = r[i+1]*a[i+1]
    # similar to the above logic but in reverse order

# calculating the individual product
for i in range(length):
    r[i] *= l[i]
print(r)
