def part1():
    data = [list(i) for i in open('input.txt','r').read().splitlines()]
    point = 0
    key = 'XMAS'
    for i in range(0,len(data)):
        for j in range(0,len(data[0])):
            for k in [0,-1,1]:
                for l in [0,-1,1]:
                    safe = True
                    for m in range(0,len(key)):
                        if i + k*m < len(data) and j + l*m < len(data[0]) and i + k*m >= 0 and j + l*m >= 0:
                            if data[i + k*m][j + l*m] != key[m]:
                                safe = False
                        else:
                            safe = False
                            continue
                    if safe == True:
                        point += 1
    return point

def part2():
    data = [list(i) for i in open('input.txt','r').read().splitlines()]
    point = 0
    for i in range(0,len(data)):
        for j in range(0,len(data[0])):
            if data[i][j] == 'A':
                try:
                    if data[i-1][j-1] == data[i+1][j+1] or data[i-1][j+1] == data[i+1][j-1]:
                        continue
                    elif data[i-1][j-1] in ['A','X'] or data[i+1][j+1] in ['A','X'] or data[i-1][j+1] in ['A','X'] or data[i+1][j-1] in ['A','X']:
                        continue
                    else:
                        point += 1                    
                except:
                    safe = False
    return point
    
print(f'Part1: {part1()}')
print(f'Part2: {part2()}')

