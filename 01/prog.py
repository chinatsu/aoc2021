f=lambda*l:sum(a<b for a,b in zip(l,l[1:]))
p=list(map(int,open(0)))
print(f(*p),f(*map(sum,zip(p,p[1:],p[2:]))))