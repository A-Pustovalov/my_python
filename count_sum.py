j=0
d=list(input())
for i in range(0,len(d)):
    if int(d[i]) % 2 !=0:
        j= j + int(d[i])*int(d[i])
print(j)
