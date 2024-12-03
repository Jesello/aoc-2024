def control(data):
    pol = int(data[1]) - int(data[0])
    for j in range(0,len(data)-1):
        diff = int(data[j + 1]) - int(data[j])
        if pol > 0 and diff >= 1 and diff <= 3:
            pass
        elif pol < 0 and diff >= -3 and diff <= -1:
            pass
        else:
            return -1
    return 1


def part1():
    data = open('input.txt','r').read().splitlines()
    count = 0
    for i in data:
        if control(i.split(' ')) == 1:
            count += 1
    return count


def part2():
    data = open('input.txt','r').read().splitlines()
    count = 0
    for i in data:
        i = i.split(' ')
        out = control(i)
        if out == 1:
            count += 1
        elif out == -1:
            for j in range(0,len(i)):
                k = i.copy()
                k.pop(j)
                if control(k) == 1:
                    count += 1
                    break
                else:
                    pass
    return count


print(f'Part1: {part1()}')
print(f'Part2: {part2()}')
