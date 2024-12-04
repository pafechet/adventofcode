with open('input.txt') as file:
    fi = file.readlines()

fi = ''.join(fi)

import re

pattern = r'mul\((\d+),(\d+)\)'
matches = re.findall(pattern, fi)

tot = 0
for match in matches:
    a, b = map(int, match)
    tot += a * b

print(tot)



mul_extracted = re.findall("don't\(\)|do\(\)|mul\(\d+,\d+\)", fi)

result = 0
enabled = bool
for instr in mul_extracted:
    if instr == "don't()":
        enabled = False
    elif instr == "do()":
        enabled = True
    elif enabled:
        n1, n2 = instr[4:len(instr) - 1].split(",")
        result += int(n1) * int(n2)
print(result)