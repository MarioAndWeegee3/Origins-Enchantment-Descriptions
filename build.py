#!/usr/bin/python3
from zipfile import ZipFile
from pathlib import Path

VERSION = '0.1.0'
NAME = 'Origins Enchantment Descriptions'

FILES = [
    Path('pack.mcmeta'),
    Path('pack.png'),
    Path('LICENSE'),
]
FILES.extend([
    path for path in Path('./assets').glob('**/*.*')
])


def main():
    build = Path('./build')
    if not build.exists():
        build.mkdir()

    with ZipFile(f'build/{NAME}-{VERSION}.zip', mode='w') as out:
        for file in FILES:
            out.write(file)


if __name__ == "__main__":
    main()
