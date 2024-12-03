def control(data):
  key = 'mul'
  allowed = list("1234567890,")
  point = 0
  
  for i in range(0,len(data)-len(key)):
        found = True
        for j in range(0,len(key)):
            if data[i+j] != key[j]:
                found = False
        if found == True and data[i+len(key)] == '(':
            chars = str()
            try:
              while data[i+len(key)+1] != ')':
                  chars += data[i+len(key)+1]
                  i += 1
            except:
              pass
            legal = True
            for j in chars:
                if j not in allowed:
                    legal = False

            if legal == True:
                try:
                    chars = chars.split(",")
                    point += int(chars[0]) * int(chars[1])
                except:
                    pass
  return point


def part1():
    data = open('input.txt','r').read()
    return control(data)


def part2():
    a_data = open('input.txt','r').read().split('do()')
    point = 0
    for data in a_data:
        data = data.split("don't()")[0]
        point += control(data)
    return point


print(f'Part1: {part1()}')
print(f'Part2: {part2()}')
