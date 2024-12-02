def is_ascending_with_conditions(my_list):
    if len(my_list) < 2:
        return False
    
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1] or not (1 <= my_list[i + 1] - my_list[i] <= 3):
            return False
    
    return True

def is_descending_with_conditions(my_list):
    if len(my_list) < 2:
        return False
    
    for i in range(len(my_list) - 1):
        if my_list[i] < my_list[i + 1] or not (1 <= my_list[i] - my_list[i + 1] <= 3):
            return False
    
    return True

def list_without_index(old_list, index):
    return old_list[:index] + old_list[index + 1:]

count = 0

with open("day_2_input.txt", 'r') as file:
    for line in file:
        values = line.strip().split()
        values = [int(value) for value in values]

        if(is_ascending_with_conditions(values) or is_descending_with_conditions(values)):
            count = count + 1
        else:
            safe = False
            for i in range(len(values)):
                new_list = list_without_index(values, i)
                if(is_ascending_with_conditions(new_list) or is_descending_with_conditions(new_list)):
                    safe = True
            if(safe):
                count = count + 1
        
print(count)