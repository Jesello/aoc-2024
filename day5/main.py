def table(rules):
    t = {}

    for i in set([j for i in rules.splitlines() for j in i.split('|')]):
        t[i] = []

    for i in rules.splitlines():
        i= i.split('|')
        t[i[0]].append(i[1])

    return t


def part1_2():
    rules,pages = open("input.txt","r").read().split("\n\n")
        
    t = table(rules)
    
    point_1 = 0
    point_2 = 0

    for i in pages.splitlines():
        i = i.split(',')
        safe = True
        for j in range(0,len(i)-1):
            if i[j+1] not in t[i[j]]:
                safe = False
        if safe == True:
            point_1 += int(i[int((len(i)-1)/2)])
        else:
            r = {}
            
            for j in i:
                order = 0
                a = i[:]
                a.remove(j)
                for k in a:
                    if k in t[j]:
                        order += 1
                r[j] = order
            sk = sorted(r.keys(), key=lambda k: r[k],reverse=True)
            point_2 += int(sk[int((len(sk)-1)/2)])
            
    print(f'Part1: {point_1}')
    print(f'Part2: {point_2}')
    
part1_2()
