f=open('2022/input/day1input.txt','r')
calories=f.read().split('\n')
counts=[]
current=0
for i in calories:
    if i=='':
        counts.append(current)
        current=0
    else:
        current+=int(i)
counts=sorted(counts)
print('part one:',counts[-1])
print('part two:',sum(counts[-3:]))

