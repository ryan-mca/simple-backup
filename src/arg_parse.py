import argparse

def start_argparse():
    parser = argparse.ArgumentParser(
        prog="Simple-Backup",
        description="A simple program to backup files.\nSupports several different compression methods",
        epilog="Licensed under GPLv3"
    )

    parser.add_argument("Original",
                        help="Original file/folder")
    parser.add_argument("Destination",
                        help="Folder to copy to")
    parser.add_argument("-c", "--compression",
                        default="zstd",
                        required=False,
                        help="Compression method to use. Supports: ZSTD (default), ZIP, GZIP, XZ, BZIP LZ4, tar, None")
    parser.add_argument("-t", "--time",
                        default=7,
                        required=True,
                        help="Amount of days to keep backups for")

    return parser