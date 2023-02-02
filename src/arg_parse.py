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

    return parser