#!/usr/bin/env python3

from libs.reverso import reverso
import sys
import argparse

def define_arguments():
    p = argparse.ArgumentParser()
    p.add_argument('-m', '--main_language',
        metavar='<language>', required=True,
        help='set the main language you want to translate from')
    p.add_argument('-f', '--foreign_language',
        metavar='<language>', required=True,
        help='set the foreign language you want to translate to')
    p.add_argument('-c', '--content',
        metavar='<content>', required=True,
        help='set the content to translate')
    return p

def get_args():
    p = define_arguments()
    if len(sys.argv) < 6:
            p.print_help()
            exit(0)
    return p.parse_args()

if __name__ == "__main__":
    r = reverso()
    args = get_args()
    words = r.translate(args.main_language, args.foreign_language, args.content)
    [print(word) for word in words if word != '']
