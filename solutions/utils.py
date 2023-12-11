import os

import requests


def save_input_file(day: int, overwrite: bool = False) -> None:
    target_file = f'day{day:02d}/task_input.txt'
    if os.path.exists(target_file) and not overwrite:
        return

    if not os.path.isdir(f'day{day:02d}'):
        os.mkdir(f'day{day:02d}')

    input_link = f"https://adventofcode.com/2023/day/{day}/input"

    if not os.path.exists('cookie.txt'):
        raise Exception(
            'No cookie file found. Save your cookie from the Advent of Code website in the solutions/cookie.txt file.'
        )

    with open('cookie.txt') as f:
        cookies = {"session": f.read()}

    response = requests.get(input_link, cookies=cookies)
    if response.status_code == 200:
        content = response.content
        content = content.replace(b'\r\n', b'\n')
        with open(f'day{day:02d}/task_input.txt', 'wb') as f:
            f.write(content)


if __name__ == '__main__':
    # test
    save_input_file(2)
