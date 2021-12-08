import numpy as np
f=open('day4input.txt','r')
lines=f.read().split('\n')
nums=[int(x) for x in lines[0].split(',')]
del lines[0]
boards=np.zeros((100,5,5))
for i, line in enumerate(lines):
    if i%6==0:
        pass
    else:
        entries=line.split()
        boards[i//6][(i-1)%6]=np.array(entries)
def part1():
    b=boards.copy()
    for num in nums:
        b[np.isin(b,num)] = -1
        for i in range(100):
            board=b[i]
            for j in range(5):
                if np.all(board[j]==-1) or np.all(np.transpose(board)[j]==-1):
                    board[np.isin(board,-1)]=0
                    score=num*(np.sum(board))
                    return score
def part2():
    b=boards.copy()
    won=[]
    for num in nums:
        b[np.isin(b,num)] = -1
        for i in range(100):
            if i not in won: 
                board=b[i]
                for j in range(5):
                    if np.all(board[j]==-1) or np.all(np.transpose(board)[j]==-1):
                        if len(won)==99:
                            board[np.isin(board,-1)]=0
                            score=num*(np.sum(board))
                            return score
                        else:
                            if i not in won:
                                won.append(i)
print(part1())
print(part2())
