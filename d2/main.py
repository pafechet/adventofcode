with open('input.txt') as fi:
    lines = fi.readlines()

def is_safe(list_):
        # Check if all levels are increasing or decreasing
        increasing = all(list_[i] < list_[i+1] for i in range(len(list_)-1))
        decreasing = all(list_[i] > list_[i+1] for i in range(len(list_)-1))
        if not (increasing or decreasing):
            return False

        # Check if any two adjacent levels differ by at least one and at most three
        for i in range(len(list_)-1):
            if abs(list_[i] - list_[i+1]) < 1 or abs(list_[i] - list_[i+1]) > 3:
                return False

        return True
safe_count=0

for line in lines:
    l_line = map(int, line.split(' '))
    if is_safe(l_line):
        safe_count += 1  
    else:
        # Check if removing a single level from the report would make it safe
        for i in range(len(l_line)):
            modified_list = l_line[:i] + l_line[i+1:]
            if is_safe(modified_list):
                safe_count += 1
                break
print(safe_count)