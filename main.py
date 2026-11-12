import json as j,os,urllib.request as u
W=[0,100,320,330,500,900,0]
Q=(-17,-16,-15,-1,1,15,16,17)
Y=[0,0,5,3,2,2,0]
FC=[0,1,2,3,3,2,1,0]
N=[0]
B=1e5
T={}
C={116:3,112:2,119:1,4:12,0:8,7:4}
class X(Exception):0
def P(p,b):
 return j.load(u.urlopen(os.getenv("MAKEFUN_ENV_URL")+p,j.dumps(b).encode()))
def A(b,q,t):
 for x in(q+15*t,q+17*t):
  if not x&136 and b[x]==t:return 1
 for o in(-33,-31,-18,-14,14,18,31,33):
  x=q+o
  if not x&136 and b[x]==2*t:return 1
 for o in Q:
  x=q+o
  if not x&136 and b[x]==6*t:return 1
  while not x&136:
   v=b[x]
   if v:
    if v==5*t or v==(3*t,4*t)[o in(-16,-1,1,16)]:return 1
    break
   x+=o
 return 0
def F(f):
 p=f.split();b=[0]*128
 for r,w in enumerate(p[0].split("/")):
  i=r*16
  for c in w:
   if c.isdigit():i+=int(c)
   else:v="PNBRQKpnbrqk".find(c);b[i]=v+1 if v<6 else 5-v;i+=1
 c=sum(1<<"KQkq".find(ch)for ch in p[2]if ch!="-")
 q=p[3];e=-1 if q=="-" else(8-int(q[1]))*16+ord(q[0])-97
 return b,1 if p[1]=="w" else-1,c,e
def K(b,s,c,e,m):
 f,t,q=m&127,(m>>7)&127,m>>14;n=b[:];v=n[f];n[t]=v;n[f]=0
 if v==s:
  if t==e:n[t+16*s]=0
  e=(f+t)//2 if abs(t-f)==32 else-1
  if q:n[t]=q*s
 else:e=-1
 if abs(v)==6 and abs(t-f)==2:
  a,d=(t+1,t-1)if t>f else(t-2,t+1);n[d]=n[a];n[a]=0
 c&=~(C.get(f,0)|C.get(t,0))
 return n,c,e
def G(b,s,c,e,cap):
 m=[]
 for i in range(128):
  v=b[i]
  if i&136 or v*s<=0:continue
  t=abs(v)
  if t==1:
   d=-16*s
   for o,cp in((d,0),(2*d,0),(d-1,1),(d+1,1)):
    x=i+o
    if x&136:continue
    if cp:
     if b[x]*s>=0 and x!=e:continue
    elif b[x] or(o==2*d and((i>>4)!=(5*s+7)//2 or b[i+d])):continue
    if x>>4 in(0,7):
     for q in(5,4,3,2):m.append((-900-100*cp-q*10,i|(x<<7)|(q<<14)))
    elif cp or not cap:
     m.append((((100-W[abs(b[x])]*10)if b[x] else-900)if cp else 0,i|(x<<7)))
  else:
   D=((-33,-31,-18,-14,14,18,31,33),(-17,-15,15,17),(-16,-1,1,16),Q,Q)[t-2]
   for o in D:
    x=i+o
    while not x&136:
     v=b[x]
     if v:
      if v*s<0:m.append((W[t]-W[abs(v)]*10,i|(x<<7)))
      break
     if not cap:m.append((0,i|(x<<7)))
     if t not in(3,4,5):break
     x+=o
   if t==6 and not cap:
    for k,bit,d,n in((116,1,1,3),(116,2,-1,4),(4,4,1,3),(4,8,-1,4)):
     if c&bit and b[k+d*n]==4*s and not any(b[k+d*j]for j in range(1,n))and not any(A(b,k+d*j,-s)for j in range(3)):m.append((0,k|((k+2*d)<<7)))
 m.sort()
 return m
def V(b,s):
 x=M=0;wk=bk=0
 for i in range(128):
  v=b[i]
  if i&136 or not v:continue
  t=abs(v);w=W[t];M+=w;f=i&7;r=i>>4;cn=2*(FC[f]+FC[r])
  if t==1:y=(6-r if v>0 else r-1)*8+cn
  elif t==6:
   if v>0:wk=i
   else:bk=i
   y=0
  else:y=cn*Y[t]+(15 if t==4 and(r==1 if v>0 else r==6)else 0)
  x+=(w+y)*v//t
 for k,g in((wk,1),(bk,-1)):
  x+=g*2*(FC[k&7]+FC[k>>4])*(4 if M<1400 else-3)
 return x if s>0 else-x
def S(b,s,c,e,d,a,be):
 N[0]+=1
 if N[0]>B:raise X
 ki=b.index(6*s)
 if d<=0:
  if A(b,ki,-s):return S(b,s,c,e,1,a,be)
  v=V(b,s)
  if v>=be:return be
  if v>a:a=v
  for sc,m in G(b,s,c,e,1):
   n,cc,ee=K(b,s,c,e,m)
   if-6*s not in n or A(n,n.index(6*s),-s):continue
   v=-S(n,-s,cc,ee,0,-be,-a)
   if v>=be:return be
   if v>a:a=v
  return a
 if len(T)>5e4:T.clear()
 k=(tuple(b),s,c,e);bm=T.get(k,0)
 l=bv=0
 ms=G(b,s,c,e,0)
 if bm:ms.sort(key=lambda z:z[1]!=bm)
 for sc,m in ms:
  n,cc,ee=K(b,s,c,e,m)
  if-6*s not in n or A(n,n.index(6*s),-s):continue
  l=1
  v=-S(n,-s,cc,ee,d-1,-be,-a)
  if v>=be:
   T[k]=m;return be
  if v>a:a=v;bv=m
 if not l:return-20000 if A(b,ki,-s)else 0
 T[k]=bv
 return a
def U(m):
 f,t,q=m&127,(m>>7)&127,m>>14
 return"%c%d%c%d%s"%(97+(f&7),8-(f>>4),97+(t&7),8-(t>>4),"nbrq"[q-2]if q else"")
def R(b,s,c,e,legal):
 N[0]=0
 ms=[m for sc,m in G(b,s,c,e,0)if U(m)in legal]
 if not ms:return legal[0]
 best=ms[0];bv=1-B
 for d in range(1,99):
  try:
   nb=best;nv=1-B
   for m in[best]+[x for x in ms if x!=best]:
    n,cc,ee=K(b,s,c,e,m)
    v=-S(n,-s,cc,ee,d-1,1-B,B-1)
    if v>nv:nv=v;nb=m
   best=nb;bv=nv
  except X:break
 return U(best)
while 1:
 g=P("/game",{})
 if g["status"]=="done":break
 if g["status"]=="your_move":
  b,s,c,e=F(g["fen"]);g=P("/move",{"game":g["game"],"move":R(b,s,c,e,g["legal_moves"])})
