with open('input.txt') as fi:
    lines = fi.readlines()

col1 = []
col2 = []

for line in lines:
    num1, num2 = map(int, line.split())
    col1.append(num1)
    col2.append(num2)

col1.sort()
col2.sort()

sum = 0

for c1, c2 in zip(col1, col2):
    tot = abs(c2 - c1)
    sum = sum +tot

value_counts_col1 = {}
for value in col1:
    value_counts_col1[value] = col2.count(value)

sum1 = 0

for value, count in value_counts_col1.items():
    sum1 = sum1 +value*count

print(sum1)