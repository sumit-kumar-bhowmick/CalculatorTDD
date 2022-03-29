import re


def add(input_string: str):

    number_list = re.findall("(\d+)", input_string)  # 1 12

    if len(number_list) == 0:
        return 0

    number_list = [int(number) for number in number_list]

    return sum(number_list)
