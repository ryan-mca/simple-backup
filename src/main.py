import argparse
from appdirs import user_config_dir

import compress

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
                        help="Compression method to use. Supports: ZSTD (default), ZIP, GZIP, XZ, BZIP LZ4, tar, None")

    args = parser.parse_args()

    comp_method = args.compression.lower()
    orig_file = args.Original
    # Removes the extra file extension as without it would create NAME.zip.zip
    dest_file = args.Destination.replace(f".{comp_method}", "")

    # Check the compression method and create the corresponding archive
    if comp_method == "zstd":
        compress.create_zstd(dest_file, orig_file)
    elif comp_method == "zip":
        compress.create_zip(dest_file, orig_file)
    elif comp_method == "gzip":
        compress.create_gzip(dest_file, orig_file)
    elif comp_method == "xz":
        compress.create_xz(dest_file, orig_file)
    elif comp_method == "bzip":
        compress.create_bzip(dest_file, orig_file)
    elif comp_method == "lz4":
        compress.create_lz4(dest_file, orig_file)
    elif comp_method == "tar":
        compress.create_tar(dest_file, orig_file)
    elif comp_method == "none":
        compress.copy(dest_file, orig_file)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("CTRL+C")