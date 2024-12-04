def count_word(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])
    word_len = len(word)
    
    def check_direction(r, c, dr, dc):
        for i in range(word_len):
            nr = r + i * dr
            nc = c + i * dc
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or matrix[nr][nc] != word[i]:
                return False
        return True

    directions = [
        (0, 1),   # Horizontal right
        (0, -1),  # Horizontal left
        (1, 0),   # Vertical down
        (-1, 0),  # Vertical up
        (1, 1),   # Diagonal down-right
        (-1, -1), # Diagonal up-left
        (1, -1),  # Diagonal down-left
        (-1, 1),  # Diagonal up-right
    ]
    
    count = 0
    
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if check_direction(r, c, dr, dc):
                    count += 1
    
    return count

def count_m_a_s_patterns(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    def check_top_left_to_bottom_right(r, c):
        return matrix[r-1][c-1] == 'M' and matrix[r+1][c+1] == 'S'

    def check_top_left_to_bottom_right_reverse(r, c):
        return matrix[r-1][c-1] == 'S' and matrix[r+1][c+1] == 'M'

    def check_top_right_to_bottom_left(r, c):
        return matrix[r-1][c+1] == 'M' and matrix[r+1][c-1] == 'S'

    def check_top_right_to_bottom_left_reverse(r, c):
        return matrix[r-1][c+1] == 'S' and matrix[r+1][c-1] == 'M'

    count = 0
    
    for r in range(1, rows-1):
        for c in range(1, cols-1):
            if matrix[r][c] == 'A':
                top_left_to_bottom_right = check_top_left_to_bottom_right(r, c)
                top_left_to_bottom_right_reverse = check_top_left_to_bottom_right_reverse(r, c)
                top_right_to_bottom_left = check_top_right_to_bottom_left(r, c)
                top_right_to_bottom_left_reverse = check_top_right_to_bottom_left_reverse(r, c)
                if(top_left_to_bottom_right and top_right_to_bottom_left):
                    count += 1
                elif(top_left_to_bottom_right and top_right_to_bottom_left_reverse):
                    count += 1
                elif(top_left_to_bottom_right_reverse and top_right_to_bottom_left):
                    count += 1
                elif(top_left_to_bottom_right_reverse and top_right_to_bottom_left_reverse):
                    count += 1

    return count

def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        matrix = [line.strip() for line in file]
    return matrix

matrix = read_matrix_from_file('day_4_input.txt')
count = count_word(matrix, 'XMAS')
print(f"The word XMAS appears {count} times in the matrix.")
count = count_m_a_s_patterns(matrix)
print(f"The X-MAS appears {count} times in the matrix.")
