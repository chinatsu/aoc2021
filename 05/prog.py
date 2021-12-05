import re
a={}
b={}
for x,y,v,w in(map(int,re.findall('\d+',x))for x in open(0)):
 for p in range(-~max(abs(v-x),abs(w-y))):c,d=(v>x)-(v<x),(w>y)-(w<y);h=x+c*p,y+d*p;b[h]=b.get(h,0)+1;a[h]=a.get(h,0)+(0==c&d)
print(*(sum(1<x[k]for k in x)for x in(a,b)))