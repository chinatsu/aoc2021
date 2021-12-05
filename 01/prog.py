p=list(map(int,open(0)))
print(*(sum(a<b for a,b in zip(p,p[i:]))for i in(1,3)))