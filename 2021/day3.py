from collections import Counter
f=open('2021/input/day3.txt','r')
nums=f.read().split('\n')
def part1():
    gamma=''
    epsilon=''
    for i in range (len(nums[0])):
        data = Counter([a[i] for a in nums])
        gamma+=data.most_common(1)[0][0]
        epsilon+=data.most_common()[1][0]
    return int(gamma,2)*int(epsilon,2)

def part2():
    l=nums
    i=0
    while len(l)>1:
        data = Counter([a[i] for a in l])
        try:
            if data.most_common()[0][1]==data.most_common()[1][1]:
                digit='1'
            else:
                digit=data.most_common()[0][0]
            l=[a for a in l if a[i]==digit]
        except IndexError:
            pass
        i+=1
    oxygen=int(l[0],2)
    m=nums
    j=0
    while len(m)>1:
        data = Counter([a[j] for a in m])
        try:
            if data.most_common()[0][1]==data.most_common()[1][1]:
                digit='0'
            else:
                digit=data.most_common()[1][0]
            m=[a for a in m if a[j]==digit]
        except IndexError:
            pass
        j+=1
    co2=int(m[0],2)
    return oxygen*co2

print('part 1:',part1())
print('part 2:',part2())
