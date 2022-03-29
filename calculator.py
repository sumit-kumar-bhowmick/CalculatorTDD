import re


def add(input_string: str):
    number_list = re.findall("(\d+|-\d+)", input_string)  # 1 12

    if len(number_list) == 0:
        return 0

    if (",\n" in input_string) or ("\n," in input_string):
        return f'''wrong input,the input contain "\\n," or ",\\n".provide any one of them as separator.ie , or \\n'''

    number_list = [int(number) for number in number_list]

    negative_numbers = list(filter(lambda x: x < 0, number_list))
    if len(negative_numbers) != 0:
        raise ValueError(f"Negative number not allowed.given negative values are {negative_numbers}")

    return sum(number_list)
