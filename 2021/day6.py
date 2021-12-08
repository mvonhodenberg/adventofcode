def numfish(days):
    f=open('day6input.txt','r').read().split(',')
    fish=[f.count(str(i)) for i in range(9)]
    for d in range(days):
        a=fish[0]
        fish[0]=0
        for i in range(0,8):
            fish[i]=fish[i+1]
        fish[6]+=a
        fish[8]=a
    return sum(fish)
print('part 1:', numfish(80))
print('part 2:', numfish(256))