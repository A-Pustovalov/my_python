h='Мой дядя самых честных правил, Когда не в шутку занемог, Он уважать себя заставил И лучше выдумать не мог'
s=h.split(' ')
for i in range(0,len(s)) :
    k=list(s[i])
    if k[0]=='м':
        s[i]=''
    d=' '.join(s[i])
    print(d)
