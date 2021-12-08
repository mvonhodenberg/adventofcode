f=open('day2input.txt','r')
commands=f.read().split('\n')
def part1():
    position=0
    depth=0
    for c in commands:
        dir=c[:-2]
        units=int(c[-1])
        if dir=='forward':
            position+=units
        if dir=='up':
            depth-= units
        if dir=='down':
            depth+=units
    print(position*depth)
def part2():
    position=0
    depth=0
    aim=0
    for c in commands:
        dir=c[:-2]
        units=int(c[-1])
        if dir=='forward':
            position+=units
            depth+=aim*units
        if dir=='up':
            aim-= units
        if dir=='down':
            aim+=units
    print(position*depth)
part1()
part2()