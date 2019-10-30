def c(k,m):
  
        z=open(k,"w")
        z.write('name,adress,age'+'\n')
        for i in range(0,len(x)):
            l=','.join(x[i])
            z.write(l+'\n')
        
        z.close
   
y="fail.txt"
x=[('ivan','ylica','56'),('gh','jjk','98')]
f=(c(y,x))
