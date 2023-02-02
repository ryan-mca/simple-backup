from appdirs import user_config_dir

import compress
import arg_parse

CONFDIR = user_config_dir("simple-backup", None)
CONFFILE = f"{CONFDIR}/config"
COMP_METHODS = ["zstd", "zip", "gzip", "xz", "bzip", "lz4", "tar", "none"]

def main():
    parser = arg_parse.start_argparse()
    args = parser.parse_args()

    comp_method = args.compression.lower()
    orig_file = args.Original
    # Removes the extra file extension as without it would create NAME.zip.zip
    dest_file = args.Destination.replace(f".{comp_method}", "")

    # Loop through the COMP_METHODS list and create the corresponding archive
    for method in COMP_METHODS:
        if comp_method == "none":
            compress.copy(dest_file, orig_file)
            return 0
        elif comp_method == method:
            func = getattr(compress, f"create_{method}")
            func(dest_file, orig_file)
            return 0

    # If the compression type isn't supported exit
    exit("Invalid compression type")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("CTRL+C")