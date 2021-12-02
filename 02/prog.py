a=h=d=0
for k,v in((k[0],int(v))for k,v in map(str.split,open(0))):
 if k=="f":h+=v;d+=v*a
 else:a+=v if k=="d"else-v
print(h*a,d*h)