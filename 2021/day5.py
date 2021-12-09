import re

f=open('2021/day5input.txt','r')
lines=f.read().split('\n')
commands=[]
for line in lines:
    a=[int(x) for x in re.split('->|,',line.replace(" ", ""))]
    commands.append([[a[0],a[1]],[a[2],a[3]]])
def part1():
    grid=[[0 for col in range(1000)] for row in range(1000)]
    for c in commands:
        if c[0][0]==c[1][0]:
            m,n=min(c[0][1],c[1][1]),max(c[0][1],c[1][1])+1
            for y in range(m,n):
                grid[y][c[0][0]]+=1
        if c[0][1]==c[1][1]:
            p,q=min(c[0][0],c[1][0]),max(c[0][0],c[1][0])+1
            for x in range(p,q):
                grid[c[0][1]][x]+=1
    return sum([sum(i > 1 for i in row) for row in grid])
def part2():
    grid=[[0 for col in range(1000)] for row in range(1000)]
    for c in commands:
        if c[0][0]==c[1][0]:
            m,n=min(c[0][1],c[1][1]),max(c[0][1],c[1][1])+1
            for y in range(m,n):
                grid[y][c[0][0]]+=1
        if c[0][1]==c[1][1]:
            p,q=min(c[0][0],c[1][0]),max(c[0][0],c[1][0])+1
            for x in range(p,q):
                grid[c[0][1]][x]+=1
        if c[1][0]-c[0][0]==c[1][1]-c[0][1]:
            s=c[1][0]-c[0][0]
            for z in range(0,abs(s)+1):
                if s>0:
                    grid[c[0][1]+z][c[0][0]+z]+=1
                if s<0:
                    grid[c[0][1]-z][c[0][0]-z]+=1
        if c[1][0]-c[0][0]==-c[1][1]+c[0][1]:
            s=c[1][0]-c[0][0]
            for z in range(0,abs(s)+1):
                if s>0:
                    grid[c[0][1]-z][c[0][0]+z]+=1
                if s<0:
                    grid[c[0][1]+z][c[0][0]-z]+=1
    return sum([sum(i > 1 for i in row) for row in grid])
print('part 1:',part1())
print('part 2:',part2())