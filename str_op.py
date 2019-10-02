s = 'У лукоморья 123 дуб зеленый 456'
print(s.index('я'))
s.count('у')
if not s.isalpha:
    print(s.upper())
if len(s)>4:
	print(s.lower())
d=list(s)
d[0]='О'
print("".join(d))
