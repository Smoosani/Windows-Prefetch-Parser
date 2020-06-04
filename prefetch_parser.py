from argparse import ArgumentParser, Namespace
from datetime import datetime, timedelta

from prefetch_win8 import *

def convert_timestamp(ts) -> str:
    dt =  datetime(1601,1,1) + timedelta(seconds=ts/10000000)
    return datetime.strftime(dt, '%Y-%m-%d %H:%M:%S')

def parse_prefetch(args: Namespace):
    """
    Args:
        args    => command line arguments (see: initalize_parser)
    Procedure:
        Extracts application information from Prefetch File
    Preconditions:
        Windows 8.1 Prefetch only
    """
    pf = PrefetchWin8.from_file(args.source)
    print("File Name: %s" % (pf.header.file_name))
    print("File Hash: %s" % (hex(pf.header.prefetch_hash).strip('0x').upper()))
    print("File Size (bytes): %s" % (pf.header.file_size))
    print("\n")
    print("Last Execution Time: %s" % (convert_timestamp(pf.fileinformation.last_execution_time)))


def initialize_parser() -> ArgumentParser:
    parser=ArgumentParser(prog="prefetch_parser", description="Parse Windows Prefetch File")
    parser.add_argument("-s",
                        "--source",
                        required=True,
                        help="Path to a single prefetch file",
                        dest="source")
    parser.set_defaults(func=parse_prefetch)
    return parser


def main() -> int:
    parser = initialize_parser()
    args = parser.parse_args()
    args.func(args)
    return 0

if __name__ == "__main__":
    main()

