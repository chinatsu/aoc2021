d=o=c=sorted([int(x,2)for x in open(0)])
f=lambda i,l:sum((x>>i)&1 for x in l)
e=lambda i,l,z:[x for x in l if(x>>i)&1==z]or l
g=0
for i in range(b:=d[-1].bit_length()):k=f(i,d)>len(d)/2;g|=k<<i
for i in range(b-1,-1,-1):u=f(i,o)>=len(o)/2;o=e(i,o,u);d=f(i,c)<len(c)/2;c=e(i,c,d)
print(g*(2**b-1^g),o[0]*c[0])