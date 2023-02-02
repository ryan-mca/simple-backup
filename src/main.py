import tarfile
import zstandard
from shutil import copy2
from appdirs import user_config_dir
from os import mkdir
from os.path import exists

CONFDIR = user_config_dir("simple-backup", None)
CONFFILE = f"{CONFDIR}/config"

def main():
    return

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("CTRL+C")