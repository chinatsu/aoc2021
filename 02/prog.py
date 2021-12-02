a=h=d=0
for k,v in((l.split()[0][0],int(l.split()[1]))for l in open(0)):
 if k=="f":h+=v;d+=v*a 
 else:a+=v if k=="d"else-v
print(f"{h*a}\n{d*h}")