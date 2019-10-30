m=-100
n=100
s=0
z=open('temper.stat.txt',"r")
a=z.read().split('\n')
for i in range(0,len(a)):
    if a[i]!='':
            g=float(a[i])
            if m<g:
                m=g
            if n>g:
                n=g
            s=s+g
d=set(a)
print("колич уник",len(d))
print("средн арифм",s/len(a),"макс",m,"мин",n)        
z.close

