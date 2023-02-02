from appdirs import user_config_dir

import compress
import arg_parse
import csv_read

CONFDIR = user_config_dir("simple-backup", None)
CONFFILE = f"{CONFDIR}/files.csv"
COMP_METHODS = ["zstd", "zip", "gzip", "xz", "bzip", "lz4", "tar", "none"]

def main():
    parser = arg_parse.start_argparse()
    args = parser.parse_args()

    comp_method = args.compression.lower()
    orig_file = args.Original
    # Removes the extra file extension as without it would create NAME.zip.zip
    dest_file = args.Destination.replace(f".{comp_method}", "").replace(".tar", "")

    # Loop through the COMP_METHODS list and create the corresponding archive
    if comp_method in COMP_METHODS:
        func = getattr(compress, f"create_{comp_method}")
        func(dest_file, orig_file)
    elif comp_method == "none":
        comp_method.copy(dest_file, orig_file)
    else:
        exit("Compression mode not supported")



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("CTRL+C")