import math
c=[int(x) for x in open('day7input.txt','r').read().split(',')]
m=math.inf
for i in range(0,len(c)):
    s=sum([abs(x-i) for x in c])
    if s<m:
        m=s
print(m)
m=math.inf
for j in range(0,len(c)):
    s=sum([int((abs(x-j)*(abs(x-j)+1))/2) for x in c])
    if s<m:
        m=s
print(m)