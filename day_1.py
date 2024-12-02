from collections import Counter
list_one = []
list_two = []
with open("day_1_input.txt", 'r') as file:
    for line in file:
        values = line.strip().split()
        
        if len(values) == 2:
            list_one.append(values[0])
            list_two.append(values[1])
sum_part_one = 0
sum_part_two = 0
list_one.sort()
list_two.sort()
for i, v in enumerate(list_one):
    #part 1
    sum_part_one += abs(int(v)- int(list_two[i])) 

    #part 2
    sum_part_two += int(v) * list_two.count(list_one[i])

print(f"Part 1 result: {sum_part_one}")
print(f"Part 2 result: {sum_part_two}")