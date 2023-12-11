import re

from solutions.utils import save_input_file

numbers_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
numbers_pattern = "|".join(numbers_dict.keys())
begin_pattern = r'^[a-z]*?(\d|' + numbers_pattern + ')'
end_pattern = r'^[a-z\d]*(\d|' + numbers_pattern + ')'


def solution(lines):
    lines = lines.split('\n')
    calibration_values = [
        int(numbers_dict.get(a, a) + numbers_dict.get(b, b)) for a, b in [
            [re.findall(begin_pattern, line)[0], re.findall(end_pattern, line)[0]]
            for line in lines if len(line) > 0
        ]]
    return sum(calibration_values)


if __name__ == '__main__':
    # test
    example = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
    assert solution(example) == 281

    # get result
    save_input_file(1)
    with open('task_input.txt') as f:
        print(solution(f.read()))
