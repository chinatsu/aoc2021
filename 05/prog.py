import re,collections as s;a=s.defaultdict(int);b=a.copy()
for x,y,v,w in(map(int,re.findall('\d+',x))for x in open(0)):
 for p in range(-~max(abs(v-x),abs(w-y))):c,d=(v-x>0)-(v-x<0),(w-y>0)-(w-y<0);h=x+c*p,y+d*p;b[h]+=1;a[h]+=1^c&d
f=lambda x:sum(x[v]>1 for v in x)
print(f(a),f(b))