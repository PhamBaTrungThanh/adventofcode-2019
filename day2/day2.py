
input_file = open('./day2/input.txt', 'r')


instructions = input_file.read().split(",")


def sequence(program_input):
    index = 0
    while index <= len(program_input) - 1:
        operation = int(program_input[index])
        if operation == 99:
            break

        first_number_index = int(program_input[index + 1])
        second_number_index = int(program_input[index + 2])
        result_location = int(program_input[index + 3])

        first_number = int(program_input[first_number_index])
        second_number = int(program_input[second_number_index])

        if (operation == 1):
            result = first_number + second_number
        if (operation == 2):
            result = first_number * second_number

        program_input[result_location] = result

        index += 4

    return program_input[0]


for i in range(99):
    for j in range(99):
        program = instructions[:]
        program[1] = i
        program[2] = j
        _result = sequence(program)
        if (_result == 19690720):
            print(i*100 + j)
            break
