#!/usr/bin/python3
def to_subtract(list_num):

    to_sub = 0
    max_lists = max(list_num)

    for n in list_num:
        if max_lists > n:
            to_sub += n

    return (max_lists -to_sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    lists_key = list(rom.keys())

    num = 0
    first_rom = 0
    list_num = [0]

    for ch in roman_string:
        for r_num in lists_key:
            if r_num == ch:
                if rom.get(ch) <= first_rom:
                    num += to_subtract(list_num)
                    list_num = [rom.get(ch)]
                else:
                    list_num.append(rom.get(ch))

                first_rom = rom.get(ch)
    num += to_subtract(list_num)
    return (num)
