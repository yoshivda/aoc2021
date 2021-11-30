import inspect
from os.path import splitext, basename
from pathlib import Path
import requests

YEAR = 2021
ROOT_PATH = Path(__file__).parents[0]


def load_input(part=''):
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    filename = module.__file__
    day = int(splitext(basename(filename))[0][3:])

    path = Path(ROOT_PATH, get_filename(day, part))
    if not path.exists():
        if not part:
            download_input(day)
        else:
            raise FileNotFoundError(f'File {path} does not exist')
    return path.read_text()


def download_input(day):
    Path(ROOT_PATH, 'inputs').mkdir(exist_ok=True)
    url = f'https://adventofcode.com/{YEAR}/day/{day}/input'
    req = requests.get(url, cookies={'session': Path(ROOT_PATH, f'credentials.secret').read_text().strip()})
    Path(ROOT_PATH, get_filename(day)).write_bytes(req.content)


def get_filename(day, part=None):
    if part:
        return f'inputs/day{str(day).zfill(2)}_{part}.txt'
    return f'inputs/day{str(day).zfill(2)}.txt'


def create_new_day():
    day = 1
    while Path(ROOT_PATH, 'days', f'day{str(day).zfill(2)}.py').exists():
        day += 1

    Path(ROOT_PATH, get_filename(day, 'small')).write_text('')
    template = Path(ROOT_PATH, 'template.py').read_text()
    Path(ROOT_PATH, 'days', f'day{str(day).zfill(2)}.py').write_text(template)


if __name__ == '__main__':
    create_new_day()
