def c(k,m):
    try:
        z=open(k,"r")
        s=open (m, "w")
        a=z.read().split('\n')
        for i in range(0,len(a)):
            s.write(str(i+1)+' '+str(a[i])+'\n')
        s.close
        z.close
    except:
        print('oshibka')
y="text.txt"
x="update_text.txt"
f=(c(y,x))
