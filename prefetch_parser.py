from argparse import ArgumentParser, Namespace

from prefetch_win8 import *

def parse_prefetch(args: Namespace):
    """
    Args:
        args    => command line arguments (see: initalize_parser)
    Procedure:
        Extracts application information from Prefetch File
    Preconditions:
        Windows 8.1 Prefetch only
    """
    pf = PrefetchWin8(args.source)
    print("File Name: %s" % (pf.header.file_name))
    print("File Hash: %s" % (pf.header.prefetch_hash))
    print("File Size (bytes): %s" % (pf.header.file_size))

def initialize_parser(): -> ArgumentParser:
    parser=ArgumentParser(prog="prefetch_parser", description="Parse Windows Prefetch File")
    parser.add_argument("-s",
                        "--source",
                        required=True,
                        help="Path to a single prefetch file",
                        dest="source")
    parser.set_defaults(func=parse_prefetch)
    return parser


def main(): -> int
    parser = initalize_parser()
    args = parser.parse_args()
    args.func(args)
    return 0

if __name__ == "__main__":
    main()

