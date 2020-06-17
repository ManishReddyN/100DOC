'''Question:
This problem was asked by Facebook.
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are de-codable. For example, '001' is not allowed.'''

message = "111"
l = len(message)
a = 1
b = 1
c = 0
for i in range(2, l+1):
    if i != 2:
        a = b
        b = c
        c = 0
    if message[i-1] != '0':
        c = b
    if message[i-2] == '1' or (message[i-1] == '2' and message[i-1] < '7'):
        c += a
print("Number Of Ways:", c)
