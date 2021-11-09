import os
import sys
import argparse
import logging
import warnings
from typing import List

sys.path.insert(1, 'src')

from pyclibase import pyclibase
prg_name = 'Example Program'
pyclibase.init_pycli(prg_name, 'example', 'example.txt')

class ExampleCLI(pyclibase.pyclibase):
    def __init__(self, args, name):
        super().__init__(args, name)

    def cmd1(self):
        super().execute_cmd('ls')


def cmd1(args, exp):
    pyclibase.log.info('running cmd1..')
    exp.cmd1()



def main(argv: List[str] = None):
    parser = argparse.ArgumentParser(prog=prg_name, description='...description...')
    parser.set_defaults(func=lambda x: parser.print_help())
    subparsers = parser.add_subparsers(title='commands')

    ##############################################################################
    # build command
    ##############################################################################
    parser_cmd1 = subparsers.add_parser(
        'cmd1',
        help='...',
        description="..."
    )
    parser_cmd1.set_defaults(func=cmd1)
    parser_cmd1.add_argument(
        '--opt1',
        type = str,
        default = 'choice1',
        choices = ['choice1', 'choice2', 'choice3'],
        help = '...'
    )

    # Execute the user command
    try:
        anyArgs = sys.argv[1:] != list()
        if anyArgs:
            args = parser.parse_args(argv)
            exp = ExampleCLI(args, prg_name)
            args.func(args, exp)
        else:
            # What purpose?
            parser.print_help()
    # Handle Ctrl-C gracefully
    except KeyboardInterrupt:
        pyclibase.log.info(f"{argv}{os.linesep}")
        sys.exit(0)


if __name__ == "__main__":
  sys.exit(main())
