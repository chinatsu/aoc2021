i=open(0).read().split("\n")
j=k=set(i)
a=""
O="1"
C="0"
e=lambda n,s:[d[n]for d in s].count(O)/len(s)
f=lambda n,s:O if e(n,s)>0.5 else C
g=lambda v:"".join([O if n==C else C for n in v])
def h(n,s,x,z):t=x if e(n,s)==0.5 else z;return[x for x in s if x[n]==t]
for n in range(len(i[0])):
 a+=f(n,i)
 if len(j)>1:j=h(n,j,O,f(n,j))
 if len(k)>1:k=h(n,k,C,g(f(n,k)))
print(int(a,2)*int(g(a),2),int(j[0],2)*int(k[0],2))