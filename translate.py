#!/usr/bin/env python3

from libs.yandex import yandex
import sys
import argparse

def define_arguments():
    p = argparse.ArgumentParser()
    p.add_argument('-l', '--language',
        metavar='<language>', required=True,
        help='set the main language you want to translate from')
    p.add_argument('-c', '--content',
        metavar='<content>', required=True,
        help='set the content to translate')
    return p

def get_args():
    p = define_arguments()
    if len(sys.argv) < 4:
            p.print_help()
            exit(0)
    return p.parse_args()

if __name__ == "__main__":
    y = yandex()
    args = get_args()
    print(y.translate(args.content, args.language))

