import argparse
import cpu
import logging


class PyNES:
    def __init__(self, args):
        self.log = logging.getLogger('PyNES')
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
                '%(asctime)s [%(name)s %(levelname)s] %(message)s',
                '%Y-%m-%d %H:%M:%S')
        handler.setFormatter(formatter)
        self.log.addHandler(handler)
        self.log.setLevel(logging.DEBUG if args.debug else logging.INFO)

        self.cpu = cpu.CPU()
        self.log.info('Initialized PyNES')


def main():
    args = parse_args()
    nes = PyNES(args)


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--debug', action='store_true',
                        help='Enable debugging output')
    return parser.parse_args()


if __name__ == '__main__':
    main()
