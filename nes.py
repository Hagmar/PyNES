import argparse
import logging


class PyNES:
    def __init__(self):
        pass


def main():
    args = parse_args()
    nes = PyNES(args)


def parse_args():
    parser = argparse.ArgumentParser()

    return parser.parse_args()


if __name__ == '__main__':
    main()
