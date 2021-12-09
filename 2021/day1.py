f=open('2021/day1input.txt','r')
depths=f.read().split('\n')
depths=[int(x) for x in depths]
def FindIncreases(l):
    c=0
    for i in range(len(l)-1):
        if l[i+1]>l[i]:
            c+=1
    return c
print('part 1:',FindIncreases(depths))
i=0
windows=[]
while i+2<len(depths):
    windows.append(sum(depths[i:i+3]))
    i+=1
print('part 2:',FindIncreases(windows))