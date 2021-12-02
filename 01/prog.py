p=list(map(int,open(0)))
f=lambda i:sum(a<b for a,b in zip(p,p[i:]))
print(f(1),f(3))