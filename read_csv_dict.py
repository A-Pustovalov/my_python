def c(k):
   try:
        z=open(k,"r")
        a=z.read().split('\n')
        for i in range(0,len(a)):
            g=a[i].split(',')
            d=dict(name=g[0],adress=g[1],age=g[2])
            a[i]=d
        return a
        z.close
   except:
        print('oshibka')
y="cf.txt"

f=(c(y))
