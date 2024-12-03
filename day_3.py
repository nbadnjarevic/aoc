import re

pattern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"
matches = []
sum = 0
do = True
with open("day_3_input.txt", 'r') as file:
    text = file.read()
    for match in re.finditer(pattern, text):
        if match.group(1) is not None and match.group(2) is not None:
            matches.append(('mul', match.group(1), match.group(2)))
        elif match.group(0) == 'do()':
            matches.append(('do',))
        elif match.group(0) == "don't()":
            matches.append(("don't",))
    for match in matches:
        if(match[0] == 'mul' and do):
            sum += int(match[1]) * int(match[2])
        if(match[0] == 'do'):
            do = True
        if(match[0] == "don't"):
            do = False
    print(sum)