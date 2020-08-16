import argparse
import os
import sys
import argparse_constants


def parse(command = None):
    parser = argparse.ArgumentParser(description="lorebox",
                                     usage="test")
    subparsers = parser.add_subparsers(dest="command")

    run_notebook = subparsers.add_parser('run', aliases=["r"], help='asg')
    showchar = subparsers.add_parser("showchar", aliases=['sc'], help="test214r41")
    print("test")

    args = parser.parse_args(command)

    if len(sys.argv[1:]) == 0:
        parser.print_help()
        print()

    return args

def start(args = None):
    if args is None:
        args = sys.argv
    print(argparse_constants.test)
    parse()

if __name__ == "__main__":
    start()
