print("Enter the weight of each item:")
a=list(map(int,input().split()))
print("Enter the profit of each item:")
b=list(map(int,input().split()))
print("maximum capacity:")
c=int(input())
d1=[]
d2=[]
for i in a:
    d=1
    e=1
    while i*d<=c:
        e=i*d
        d+=1
    d1.append(e)
for i in range(len(d1)):
    if d1[i]==a[i]:
        d2.append(b[i])
    else:
        d2.append((b[i]//a[i])*d1[i])
h=d2.index(max(d2))
print('Max profit: '+str(d2[h]))    
