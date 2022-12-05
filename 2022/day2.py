f=open('2022/input/day2input.txt','r')
l=f.read().split('\n')
def score(s):
    p1=ord(s[0])-64
    p2=ord(s[2])-87
    a= (p1-p2)%3
    if a==0 or a==1:
        a=1-a
    return(3*a+p2)
print('first part:',sum([score(x) for x in l]))
def lose(x):
    if x==1:
        return 3
    elif x==2:
        return 1
    else:
        return 2
def win(x):
    if x==1:
        return 2
    elif x==2:
        return 3
    else:
        return 1
def score2(s):
    p1=ord(s[0])-64
    p2=ord(s[2])-87
    if p2==1:
        return lose(p1)
    elif p2==2:
        return p1 +3
    else:
        return win(p1)+6
print('part 2:',sum([score2(x) for x in l]))