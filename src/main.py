import argparse
from appdirs import user_config_dir

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

    elif comp_method == "tar":
        make_archive(dest_file, "tar", orig_file)

    elif comp_method == "zip":
        make_archive(dest_file, "zip", orig_file)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("CTRL+C")