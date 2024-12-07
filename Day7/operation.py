from tqdm import tqdm

def recursive_check(column_1, column_2):
    test_value = column_1
    values = column_2
    if isinstance(values[0], str):
        values = [x for x in values[0].split(' ') if x]
        values = [int(x) if x.isnumeric() else x for x in values]
    if len(values) == 1:
        return test_value == values[0]
    # Apply the operation first_column - values[-1] and keep the values[:-1] in the 2nd column
    new_column_2 = [values[0] + values[1]] +values[2:]
    if recursive_check(column_1, new_column_2):
        return True
    new_column_2 = [values[0] * values[1]] + values[2:]
    if recursive_check(column_1, new_column_2):
        return True
    return False

def recursive_check_with_concat(column_1, column_2):
    test_value = column_1
    values = column_2
    if isinstance(values[0], str):
        values = [x for x in values[0].split(' ') if x]
        values = [int(x) if x.isnumeric() else x for x in values]
    if len(values) == 1:
        return test_value == values[0]
    # Apply the operation first_column - values[-1] and keep the values[:-1] in the 2nd column
    new_column_2 = [values[0] + values[1]] +values[2:]
    if recursive_check_with_concat(column_1, new_column_2):
        return True
    new_column_2 = [values[0] * values[1]] + values[2:]
    if recursive_check_with_concat(column_1, new_column_2):
        return True
    new_column_2 =[int(str(values[0]) + str(values[1]))] +values[2:]
    if new_column_2==None:
        return False
    if recursive_check_with_concat(column_1, new_column_2):
        return True
    return False


def main():
    with open("./Day7/file.csv", "r") as file:
        lines = file.readlines()
    
    sum = 0
    sum2 = 0
    
    for line in tqdm(lines):
        parts = line.strip().split(":")
        column_1 = int(parts[0])
        values = [x for x in parts[1].split(' ') if x]
        values = [int(x) if x.isnumeric() else x for x in values]
        check = recursive_check(column_1, values)
        if check:
            sum += column_1
        check2 = recursive_check_with_concat(column_1, values)
        if check2:
            sum2 += column_1

    print("Answer to part 1: ", sum)
    print("Answer to part 2: ", sum2)

if __name__ == "__main__":
    main()
