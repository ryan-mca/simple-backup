import zstd
import argparse
from shutil import make_archive, copy2
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
                        help="Compression method to use. Supports: ZSTD (default), ZIP, GZIP, LZ4, tar, None")

    args = parser.parse_args()

    comp_method = args.compression.lower()
    orig_file = args.Original
    # Removes the extra file extension as without it would create NAME.zip.zip
    dest_file = args.Destination.replace(f".{comp_method}", "")
    print(dest_file)

    # Check the compression method and create the corresponding archive
    if comp_method == "zstd":
        # Creates a tar archive
        make_archive(dest_file.replace(".tar", ""), "tar", orig_file)

        # Opens the tar archive and then reads the data
        with open(f"{dest_file}.tar", 'rb') as file:
            data = file.read()

        compressed_data = zstd.compress(data)

        # Writes the data
        with open(f"{dest_file}.tar.zst", 'wb') as file:
            file.write(compressed_data)

    elif comp_method == "zip":
        make_archive(args.Destination.replace(".zip", ""), "zip", args.Original)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("CTRL+C")