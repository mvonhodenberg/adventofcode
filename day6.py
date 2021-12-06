def numfish(days):
    f=open('day6input.txt','r').read().split(',')
    fish=[[i,f.count(str(i))] for i in range(9)]
    for d in range(days):
        a=fish[0][1]
        fish[0][1]=0
        for i in range(0,8):
            fish[i][1]=fish[i+1][1]
        fish[6][1]+=a
        fish[8][1]=a
    return sum([f[1] for f in fish])
print('part 1:', numfish(80))
print('part 2:', numfish(256))