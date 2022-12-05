f=open('2022/input/day3input.txt','r')
rucksacks=f.read().split('\n')
prioritysum=0
def priority(char):
    return ord(char)-96 if char.islower() else ord(char)-38
for rucksack in rucksacks:
    x=set(rucksack[:len(rucksack)//2]).intersection(set(rucksack[len(rucksack)//2:])).pop()
    prioritysum+=priority(x)
print('part 1',prioritysum)
prioritysum2=0
for i in range(0,len(rucksacks),3):
    x=set(rucksacks[i]).intersection(set(rucksacks[i+1])).intersection(set(rucksacks[i+2])).pop()
    prioritysum2+=priority(x)
print('part 2',prioritysum2)
