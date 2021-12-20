import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


data = open(os.path.join(__location__, 'day3.txt')).read().splitlines()

init_size = len(data[0])

def get_final_number(zeros_and_ones, all_numbers, current_bit_pos, criteria, init_size):
    if (len(all_numbers) == 1):
        return all_numbers
    else:
        zeros_and_ones = calculate_common_bit(init_size, all_numbers)
        common_bit = most_common_bit(zeros_and_ones, current_bit_pos, criteria)
        _selection = []
        for number in all_numbers:
            if number[current_bit_pos] == common_bit:
                _selection.append(number)


        current_bit_pos = current_bit_pos + 1
        return get_final_number(zeros_and_ones, _selection, current_bit_pos, criteria, init_size)

def most_common_bit(zeros_and_ones, i, criteria):
    # Most common bit
    total_zeros = zeros_and_ones[i]['zero']
    total_ones = zeros_and_ones[i]['one']


    if criteria == 'oxygen':
        if total_zeros > total_ones:
            return '0'
        elif total_ones > total_zeros:
            return '1'
        elif total_ones == total_zeros:
            return '1'
    else:
        if total_zeros < total_ones:
            return '0'
        elif total_ones < total_zeros:
            return '1'
        elif total_ones == total_zeros:
            return '0'

def calculate_common_bit(init_size, all_numbers):
    zeros_and_ones = []
    for i in range(init_size):
        zeros_and_ones.append(dict(one=0, zero=0))

    for number in all_numbers:
        for index, n in enumerate(number):
            if n == '0':
                zeros_and_ones[index]['zero'] = zeros_and_ones[index]['zero'] + 1
            elif n == '1':
                zeros_and_ones[index]['one'] = zeros_and_ones[index]['one'] + 1

    return zeros_and_ones

def run():
    zeros_and_ones = calculate_common_bit(init_size, data)
    oxygen_num = get_final_number(zeros_and_ones, data, 0, 'oxygen', init_size)[0]
    co2_num = get_final_number(zeros_and_ones, data, 0, 'co2', init_size)[0]

    print("Oxygen binary result is: {}, which is {} in decimal".format(oxygen_num,int(oxygen_num, 2)))
    print("Co2 binary result is: {}, which is {} in decimal".format(co2_num,int(co2_num, 2)))

    print("Final result is {}".format(int(oxygen_num, 2) * int(co2_num, 2)))

run()
