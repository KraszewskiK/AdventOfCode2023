import re


def solution(lines):
    lines = lines.split('\n')
    calibration_values = [
        int(re.findall(r'^[a-z]*(\d)', line)[0] + re.findall(r'(\d)[a-z]*$', line)[0])
        for line in lines
    ]
    return sum(calibration_values)


if __name__ == '__main__':
    # test
    example = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
    assert solution(example) == 142

    with open('task_input.txt') as f:
        print(solution(f.read()))
