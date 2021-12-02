from typing import Counter


f=open('day1input.txt','r')
depths=f.read().split('\n')
depths=[int(x) for x in depths]
def FindIncreases(l):
    c=0
    for i in range(len(l)-1):
        if l[i+1]>l[i]:
            c+=1
    return c
def part1():
    print(FindIncreases(depths))
def part2():
    i=0
    windows=[]
    while i+2<len(depths):
        windows.append(sum(depths[i:i+3]))
        i+=1
    print(FindIncreases(windows))
part1()
part2()