import argparse
import os
import sys
from util.argparse_constants import *
import util.cli as cli

def parse(command = None):
    parser = argparse.ArgumentParser(description="lorebox",
                                     usage="test")
    subparsers = parser.add_subparsers(dest="command")

    showchar = subparsers.add_parser("showchar", aliases=['sc'], help=showchar_help)
    showchar.add_argument("character", help=showchar_character_help)
    showchar.set_defaults(which=showchar_cmd)

    args = parser.parse_args(command)

    if len(sys.argv[1:]) == 0:
        parser.print_help()
        print()

    return args

def start(args = None):
    if args is None:
        args = sys.argv
    func = cli.command(parse())


if __name__ == "__main__":
    start()
