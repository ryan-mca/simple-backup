from appdirs import user_config_dir

import compress
import arg_parse
import csv_read

CONFDIR = user_config_dir("simple-backup", None)
CONFFILE = f"{CONFDIR}/files.csv"

def main():
    parser = arg_parse.start_argparse()
    args = parser.parse_args()

    comp_method = args.compression.lower()
    orig_file = args.Original
    # Removes the extra file extension as without it would create NAME.zip.zip
    dest_file = args.Destination.replace(f".{comp_method}", "").replace(".tar", "")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("CTRL+C")