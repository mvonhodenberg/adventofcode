from queue import PriorityQueue

f=open('2021/input/day15.txt','r').read().split('\n')
map=[]
for line in f:
    map.append([int(char) for char in line])

def ReturnAdjacent(i,j,m):
    l=[]
    if i!=m-1:
        l.append((i+1,j))
    if i!=0:
        l.append((i-1,j))
    if j!=m-1:
        l.append((i,j+1))
    if j!=0:
        l.append((i,j-1))
    return l

def Dijkstra(grid):
    m=len(grid)
    distances=PriorityQueue()
    distances.put((0,(0, 0)))
    visited = {(0, 0),}
    while distances:
        risk,(i, j) = distances.get()
        if (i,j)==(m-1,m-1):
            return risk
        for (x,y) in ReturnAdjacent(i,j,m):
            if (x, y) not in visited:
                distances.put((risk + grid[x][y],(x, y)))
                visited.add((x, y))

def IncreaseLevel(n,k):
    return 9 if n+k==9 else (n+k)%9
def BigGrid(grid):
    m=len(grid)
    for i in range(m):
        x=[]
        for j in range(1,5):
            x+=[IncreaseLevel(n,j) for n in grid[i]]
        grid[i]+=x
    for k in range(1,5):
        for p in range(m):
            grid.append([IncreaseLevel(n,k) for n in grid[p]])
    return grid

print('part 1:',Dijkstra(map))
print('part 2:',Dijkstra(BigGrid(map)))