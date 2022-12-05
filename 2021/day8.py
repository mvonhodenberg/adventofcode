from itertools import groupby
lines=open('2021/input/day8.txt','r').read().split('\n')
s=0
for line in lines:
    l=line.split('|')[1].split()
    for x in l:
        if len(x) in (2,3,4,7):
            s+=1
print('part 1:',s)

def DecodeDigits(line):
    digits={'abcefg':0,'cf':1,'acdeg':2,'acdfg':3,'bcdf':4,'abdfg':5,'abdefg':6,'acf':7,'abcdefg':8,'abcdfg':9}
    inputmap={}
    inputs, outputs =line.split('|')[0].split(), line.split('|')[1].split()
    d={i:[] for i in range(2,8)}
    for word in inputs:
        d[len(word)].append(word)
    inputmap['a']=set(d[3][0]).difference(set(d[2][0])).pop()
    c_and_f=set(str(d[2][0]))
    b_and_d=set(d[4][0]).difference(set(d[2][0]))
    for s in d[6]:
        r=set('abcdefg').difference(set(s)).pop()
        if r in c_and_f:
            inputmap['c']=r
            inputmap['f']=c_and_f.difference(set(r)).pop()
        elif r in b_and_d:
            inputmap['d']=r
            inputmap['b']=b_and_d.difference(set(r)).pop()
        else:
            inputmap['e']=r
    ng=''
    for value in inputmap.values():
        ng+=value
    inputmap['g']=set('abcdefg').difference(set(ng)).pop()
    inputmap= {v: k for k, v in inputmap.items()}
    no=''
    for o in outputs:
        mapped=''
        for char in o:
            mapped+=inputmap[char]
        for digit,key in enumerate(digits):
            if set(mapped)==set(key):
                no+=str(digit)
    return int(no)

print('part 2:', sum([DecodeDigits(line) for line in lines]))