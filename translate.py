#!/usr/bin/env python3

from libs.reverso import reverso
import sys


if __name__ == "__main__":
    r = reverso()
    words = r.translate(' '.join(sys.argv[1:]))
    [print(word) for word in words]
