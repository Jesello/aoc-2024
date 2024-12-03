def part1():
    data = [i.split("   ") for i in open("input.txt","r").read().splitlines()]
    datax = sorted([int(i[0]) for i in data])
    datay = sorted([int(i[1]) for i in data])
    
    return sum([abs(datax[i]-datay[i]) for i in range(0,len(datax))])


def part2():
    data = [i.split("   ") for i in open("input.txt","r").read().splitlines()]
    datax = sorted([int(i[0]) for i in data])
    datay = sorted([int(i[1]) for i in data])

    rate = 0

    for i in datax:
        rate += datay.count(i)

    return rate


print(f'Part1: {part1()}')
print(f'Part2: {part2()}')
