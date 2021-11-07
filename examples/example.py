import os
import sys
import argparse
import logging
import warnings
from typing import List

#from rich.logging import RichHandler
#from rich import traceback
#from rich import print

from pyclibase import pyclibase
prg_name = 'Example Program'
pyclibase.print_title(prg_name, 'example')


class ExampleCLI(pyclibase.pyclibase):
    def __init__(self, args, name):
        super().__init__(args, name)


def cmd1(args,):
    print('clean')


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
        'opt1',
        type = str,
        default = 'choice1',
        choices = ['choice1', 'choice2', 'choice3e'],
        help = '...'
    )

    # Execute the user command
    try:
        anyArgs = sys.argv[1:] != list()
        if anyArgs:
            args = parser.parse_args(argv)
            exp = Example(arg, prg_name)
            args.func(args, exp)
        else:
            # What purpose?
            parser.print_help()
    # Handle Ctrl-C gracefully
    except KeyboardInterrupt:
        print(f"{argv}{os.linesep}")
        sys.exit(0)


if __name__ == "__main__":
  sys.exit(main())
