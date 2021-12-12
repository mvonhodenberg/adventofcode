from collections import Counter

f=open('2021/input/day12input.txt','r').read().split('\n')
connections={}
for line in f:
    [a,b]=line.split('-')
    try:
        connections[a].append(b)
    except KeyError:
        connections[a]=[b]
    try:
        connections[b].append(a)
    except KeyError:
        connections[b]=[a]
allpaths1=[]
allpaths2=[]
def FindPaths1(path):
    visited=[x for x in path if x.islower()]
    c=path[-1]
    for next in connections[c]:
        if next=='end':
            allpaths1.append(path+['end'])
        elif next not in visited:
            FindPaths1(path+[next])
def FindPaths2(path):
    visited=[x for x in path if x.islower()]
    c=path[-1]
    for next in connections[c]:
        if next=='end':
            allpaths2.append(path+['end'])
        elif visited.count(next)==0:
            FindPaths2(path+[next])
        elif visited.count(next)==1 and next!='start':
            if Counter(visited).most_common()[0][1]==1:
                FindPaths2(path+[next])
FindPaths1(['start'])
FindPaths2(['start'])
print('part 1:',len(allpaths1))
print('part 2:',len(allpaths2))
