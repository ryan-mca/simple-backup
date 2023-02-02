import tarfile
import zstandard
import argparse
from shutil import make_archive
from appdirs import user_config_dir
from os import mkdir
from os.path import exists

CONFDIR = user_config_dir("simple-backup", None)
CONFFILE = f"{CONFDIR}/config"

def main():
    # Set up argparser
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
                        help="Compression method to use. Supports: ZSTD (default), ZIP, GZIP, LZ4, None")

    args = parser.parse_args()

    comp_method = args.compression.lower()

    if comp_method == "zip":
        make_archive(args.Destination, "zip", args.Original)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("CTRL+C")