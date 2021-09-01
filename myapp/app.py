import argparse
import os
import sys
from pathlib import Path

textchars = bytearray({7, 8, 9, 10, 12, 13, 27} | set(range(0x20, 0x100)) - {0x7F})


def is_binary_string(bytes_text):
    return bool(bytes_text.translate(None, textchars))


def find_all_lines(x, word):
    number = 1
    ans = []
    for i in open(x, encoding='utf-8', errors='ignore'):
        if str(i).find(word) >= 0:
            st = f'{x.name} line={number}: {i}'
            ans.append(st)
        number += 1
    return ans


def find(path, word):
    for path2 in os.walk(path):
        for name in path2[2]:
            x = Path(os.path.join(path2[0], name))
            if not x.is_file() or is_binary_string(open(x, 'rb').read(1024)):
                continue

            ans = find_all_lines(x, word)

            for i in ans:
                print(i, end='')


def parser_help(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='path, where you want to start', type=str)
    parser.add_argument('word', help='word, which you want to find', type=str)
    return parser.parse_args(args)


def main(save_args=None):
    if save_args is None:
        save_args = parser_help(sys.argv[1:])
    find(Path(save_args.path), save_args.word)
