f=open('2021/input/day11input.txt','r').read().split('\n')
grid=[]
for line in f:
    grid.append([int(char) for char in line])
m=len(grid)
def incrementby1(i,j,g):
    if i!=0:
        g[i-1,j]+=1
        if j!=0:
            g[i,j-1]+=1
        if j!=m:
            g[i-1,j+1]+=1
    if i!=m:
        g[i+1,j]+=1
        if j!=m:
            g[i+1,j+1]+=1
        if j!=0:
            g[i+1,j-1]+=1
    if j!=0:
        g[i,j-1]+=1
    if j!=m:
        g[i,j+1]+=1
    return g
def flash(g):
    flashcounter=0
    flashed=([0]*m)*m
    for i in range(m):
        for j in range(m):
            if g[i][j]==9:
                g=incrementby1(i,j,g)
                flashcounter+=1
                g[i][j]=0
    return g