from os.path import commonprefix
from copy import deepcopy


def solution1(diagnostics):
    diagnostic_len = len(diagnostics[0])
    diagnostics_count = len(diagnostics)
    gamma_rate = ''
    epsilon_rate = ''
    for i in range(diagnostic_len):
        bit_sum = 0
        for d in diagnostics:
            bit_sum += int(d[i])
        if bit_sum >= diagnostics_count / 2:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'
    power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
    return power_consumption


def solution2(diagnostics):
    diagnostic_len = len(diagnostics[0])
    oxygen_diagnostics = deepcopy(diagnostics)
    co2_diagnostics = deepcopy(diagnostics)

    for i in range(diagnostic_len):
        if len(oxygen_diagnostics) == 1:
            break
        bit_sum = 0
        for d in oxygen_diagnostics:
            bit_sum += int(d[i])
        if bit_sum >= len(oxygen_diagnostics) / 2:
            mode_bit = '1'
        else:
            mode_bit = '0'
        d_i = 0
        while d_i < len(oxygen_diagnostics):
            if oxygen_diagnostics[d_i][i] != mode_bit:
                oxygen_diagnostics.remove(oxygen_diagnostics[d_i])
                d_i -= 1
                if len(oxygen_diagnostics) == 1:
                    break
            d_i += 1

    for i in range(diagnostic_len):
        if len(co2_diagnostics) == 1:
            break
        bit_sum = 0
        for d in co2_diagnostics:
            bit_sum += int(d[i])
        if bit_sum >= len(co2_diagnostics) / 2:
            anti_mode_bit = '0'
        else:
            anti_mode_bit = '1'
        d_i = 0
        while d_i < len(co2_diagnostics):
            if co2_diagnostics[d_i][i] != anti_mode_bit:
                co2_diagnostics.remove(co2_diagnostics[d_i])
                d_i -= 1
                if len(co2_diagnostics) == 1:
                    break
            d_i += 1

    oxygen_generator_rating = int(oxygen_diagnostics[0], 2)
    co2_generator_rating = int(co2_diagnostics[0], 2)
    life_support_rating = oxygen_generator_rating * co2_generator_rating
    return life_support_rating


if __name__ == "__main__":
    with open("input.txt") as file:
        f_in = file.read().splitlines()
    print(solution1(f_in))
    print(solution2(f_in))
