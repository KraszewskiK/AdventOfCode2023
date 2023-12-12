import os

import requests

COOKIE = ""  # fill with your cookie from https://adventofcode.com/


def save_input_file(day: int, overwrite: bool = False) -> None:
    target_file = 'task_input.txt'
    if os.path.exists(target_file) and not overwrite:
        return

    input_link = f"https://adventofcode.com/2023/day/{day}/input"

    if not COOKIE:
        raise Exception(
            'No cookie found. \
Save your cookie from the Advent of Code website to the COOKIE variable in the solutions/utils.py file.'
        )

    cookies = {"session": COOKIE}

    response = requests.get(input_link, cookies=cookies)
    if response.status_code == 200:
        content = response.content
        content = content.replace(b'\r\n', b'\n')
        with open(target_file, 'wb') as f:
            f.write(content)


def create_file_structure(days: int = 25):
    with open("templates/task_template") as f:
        task_template = f.read()
    with open("templates/README_template") as f:
        readme_template = f.read()
    for day in range(1, days + 1):
        # day* directory
        if not os.path.exists(f'day{day:02d}'):
            os.mkdir(f'day{day:02d}')
        # day*/README.md file
        if not os.path.exists(f'day{day:02d}/README.md'):
            with open(f'day{day:02d}/README.md', 'w') as f:
                f.write(readme_template.format(day=day))
        # day*/task1.py file
        if not os.path.exists(f'day{day:02d}/task1.py'):
            with open(f'day{day:02d}/task1.py', 'w') as f:
                f.write(task_template.format(day))
        # day*/task2.py file
        if not os.path.exists(f'day{day:02d}/task2.py'):
            with open(f'day{day:02d}/task2.py', 'w') as f:
                f.write(task_template.format(day))


if __name__ == '__main__':
    create_file_structure(2)
