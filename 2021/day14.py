f=open('2021\input\day14.txt').read().split('\n')
polymer=f[0]
rules=dict([r.strip().split(' -> ') for r in f[2:]])
freq={x:0 for x in rules}
counts={letter:polymer.count(letter) for letter in rules.values()}
for j in range(len(polymer)-1):
    freq[polymer[j:j+2]]+=1

def Step(f,c):
    out={x:0 for x in f}
    for pair in f:
        out[pair[0]+rules[pair]]+=f[pair]
        out[rules[pair]+pair[1]]+=f[pair]
        c[rules[pair]]+=f[pair]
    return out,c
def Output(no_steps,f,c):
    for i in range(no_steps):
        f,c=Step(f,c)
    qty=list(c.values())
    return max(qty)-min(qty)

print('part 1:',Output(10,freq,counts))
print('part 2:',Output(40,freq,counts))