lines=open('2021/input/day10input.txt','r').read().split('\n')
pairs={'(':')','{':'}','[':']','<':'>'}
corruptscores={')':3,']': 57,'}':1197,'>':25137}
completescores={')':1,']': 2,'}':3,'>':4}
errorscore=0
for i,line in enumerate(lines):
    s=''
    for char in line:
        if char in pairs:
            s+=char
        if char in pairs.values():
            if (False if s=='' else (pairs[s[-1]]==char)):
                s=s[:-1]
            else:
                errorscore+=corruptscores[char]
                lines[i]+='x'
                break
print('part 1:',errorscore)
lines=[line for line in lines if line[-1]!='x']
def ScoreLine(line):
    s=''
    r=''
    for char in line:
        if char in pairs:
            s+=char
        if char in pairs.values():
            if (False if s=='' else (pairs[s[-1]]==char)):
                s=s[:-1]
    s=s[::-1]
    for char in s:
        r+=pairs[char]
    out=0
    for a in r:
        out=5*out + completescores[a]
    return out
scores=[]
for line in lines:
    scores.append(ScoreLine(line))
print('part 2:',sorted(scores)[len(scores)//2])

