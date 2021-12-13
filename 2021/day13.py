import numpy as np
f=open('2021\input\day13input.txt').read().split('\n')
width,height=0,0
coords=[]
folds=[]
for line in f:
    if ',' in line:
        [a,b]=[int(x) for x in line.split(',')]
        coords.append((a,b))
        if a>width:
            width=a
        if b>height:
            height=b
    if line[:4]=='fold':
        folds.append((line.split('=')[0][-1],int(line.split('=')[1])))
grid=np.zeros((width+1,height+1))
print(np.shape(grid))
for x in coords:
    grid[x[0]][x[1]]=1
def FoldPaper(axis,n,grid):
    a=len(grid)
    b=len(grid[0])
    if axis=='x':
        for i in range(n,a):
            for j in range(b):
                if grid[i][j]==1:
                    grid[a-1-i][j]=1
        grid=grid[:n,:]
        return grid,np.sum(grid)
    if axis=='y':
        for i in range(a):
            for j in range(n,b):
                if grid[i][j]==1:
                    grid[i][b-1-j]=1
        grid=grid[:,:n]
        return grid,np.sum(grid)
print('part 1:',FoldPaper('x',655,grid)[1])
for fold in folds:
    grid=FoldPaper(fold[0],fold[1],grid)[0]
print(grid)
print('part 2: RPCKFBLR')