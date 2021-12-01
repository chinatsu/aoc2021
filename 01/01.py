f=lambda l:print(sum(a<b for a,b in zip(l,l[1:])))
f(p:=list(map(int,open("in"))))
f(list(map(sum,zip(p,p[1:],p[2:]))))