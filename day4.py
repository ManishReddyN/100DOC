l = [3, 4, -1, 1,2,5,6,10]
k = [i for i in l if i > 0]
length = len(k)
flag=length+2
check=0
for i in range(length):
    if(k[i]>length):
        k[i]=flag
for i in range(length):
    if k[i]==flag:
        continue
    v=abs(k[i])
    k[v-1]*=-1
for i in range(length):
    if k[i]>0:
        print(i+1)
        check=1
        break
if check==0:
    print(length+1)