f=open('2021/input/day9.txt','r').read().split('\n')
grid=[]
for line in f:
    grid.append([int(char) for char in line])
m=len(grid)
s=0
basins={}
for i in range(m):
    for j in range(m):
        n=grid[i][j]
        c1=True if i==0 else (n<grid[i-1][j])
        c2=True if i==m-1 else (n<grid[i+1][j])
        c3=True if j==0 else (n<grid[i][j-1])
        c4=True if j==m-1 else (n<grid[i][j+1])
        if c1 and c2 and c3 and c4:
            s+=n+1
            basins[i,j]={(i,j)}
print('part 1:',s)
def FindNeighbours(i,j):
        l=[]
        if (False if i==0 else (grid[i][j]<grid[i-1][j] and grid[i-1][j]<9)):
            l.append((i-1,j))
        if (False if i==m-1 else (grid[i][j]<grid[i+1][j] and grid[i+1][j]<9)):
            l.append((i+1,j))
        if (False if j==0 else (grid[i][j]<grid[i][j-1] and grid[i][j-1]<9)):
            l.append((i,j-1))
        if (False if j==m-1 else (grid[i][j]<grid[i][j+1] and grid[i][j+1]<9)):
            l.append((i,j+1))
        return l
def FindBasin(x):
    i,j=x
    a={(i,j)}
    for neighbour in FindNeighbours(i,j):
        a=set.union(a,FindBasin(neighbour))
    return a
basinsizes=[]
for lp in basins:
    basinsizes.append(len(FindBasin(lp)))
ans=1
for x in sorted(basinsizes)[-3:]:
    ans*=x
print('part 2:',ans)