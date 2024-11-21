def check_row_column(target, nums):
    possible_rows = []
    possible_multiples = []
    for num in nums:
        if target % num == 0:
            possible_multiples.append(num)
    length = len(possible_multiples)
    index_one = 0
    index_two = 1
    index_three = 2
    for i in range(length - 2):
        index_one = i
        index_two = index_one + 1
        index_three = index_two + 1
        product = possible_multiples[index_one] * possible_multiples[index_two] * possible_multiples[index_three] 
        if product == target:
            possible_rows.append([possible_multiples[index_one], possible_multiples[index_two], possible_multiples[index_three]])
            continue
        elif product > target:
            continue
        else:
            for j in range(index_two, length - 1):
                index_two = j
                index_three = index_two + 1
                product = possible_multiples[index_one] * possible_multiples[index_two] * possible_multiples[index_three]
                if product == target:
                    possible_rows.append([possible_multiples[index_one], possible_multiples[index_two], possible_multiples[index_three]])
                    continue
                elif product > target:
                    continue
                elif product < target:
                    for k in range(index_three, length):
                        index_three = k
                        product = possible_multiples[index_one] * possible_multiples[index_two] * possible_multiples[index_three]
                        if product > target:
                            break
                        elif product == target:
                            possible_rows.append([possible_multiples[index_one], possible_multiples[index_two], possible_multiples[index_three]])
                            continue
    return possible_rows

def compare_options(nums, row_targets, column_targets):
    potential_rows = []
    potential_columns = []
    for target in row_targets:
        options = check_row_column(target, nums)
        potential_rows.append(options)
    for target in column_targets:
        options = check_row_column(target, nums)
        potential_columns.append(options)
    potential_row_positions = [[[],[],[]],[[],[],[]],[[],[],[]]]
    for row_index, potential_row in enumerate(potential_rows):
        for row in potential_row:
            for value in row:
                for column_index, divisor in enumerate(column_targets):
                    if divisor % value == 0:
                        if value not in potential_row_positions[row_index][column_index]:
                            potential_row_positions[row_index][column_index].append(value)
    finished_array = [[0,0,0], [0,0,0], [0,0,0]]
    numbers_sorted = 0
    values_confirmed = {
                    '1': 0,
                    '2': 0,
                    '3': 0,
                    '4': 0,
                    '5': 0,
                    '6': 0,
                    '7': 0,
                    '8': 0,
                    '9': 0
                }
    while numbers_sorted < 9:
        for row_index, working_row in enumerate(potential_row_positions):
            for column_index, column in enumerate(working_row):
                for row_value in column:
                    if len(column) == 1 and values_confirmed[str(row_value)] == 0:
                        values_confirmed[str(row_value)] = 1
                        finished_array[row_index][column_index] = row_value
                        numbers_sorted += 1
                    if values_confirmed[str(row_value)] == 1:
                        column.remove(row_value)
                if column == []:
                    column_indices = [0, 1, 2]
                    column_indices.remove(column_index)
                    given_number = finished_array[row_index][column_index]
                    working_index = column_indices[0]
                    checking_index = column_indices[1]
                    
                    for working_value in working_row[working_index]:
                        checking_number = int(row_targets[row_index] / given_number / working_value)
                        if checking_number not in working_row[checking_index]:
                            working_row[working_index].remove(working_value)
                    
                    row_indices = [0,1,2]
                    row_indices.remove(row_index)
                    working_row_index = row_indices[0]
                    checking_row_index = row_indices[1]
                    full_column = []
                    for row in potential_row_positions:
                        full_column.append(row[column_index])
                    for working_row_value in full_column[working_row_index]:
                        checking_number = int(column_targets[column_index] / given_number / working_value)
                        if checking_number not in full_column[checking_row_index]:
                            potential_row_positions[working_row_index][column_index].remove(working_row_value)
    return finished_array
   
if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7,8,9]
    row_targets = [56, 135, 48]
    column_targets = [21, 108, 160]
    answer = compare_options(nums, row_targets, column_targets)
    for row in answer:
        print(f'{row[0]} {row[1]} {row[2]}')