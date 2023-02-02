import configparser
from os import mkdir
from os.path import exists

def parse_configs(conffile: str):
    """Parses passes in config file and returns the compression method

    Args:
        conffile (String): Path to the config file

    Returns:
        String: The compression method
    """

    config = configparser.ConfigParser()

    config.read(conffile)

    comp_method = config["Config"]["Compression"]

    return comp_method

def set_default_config(confdir: str, conffile: str):
    """Creates a default config file at the given folder and name

    Args:
        confdir (String): Dir to create the config file in
        conffile (String): Path to the config file
    """

    config = configparser.ConfigParser()

    if not exists(confdir):
        mkdir(confdir)

    if not exists(conffile):
        config["Config"] = {"Compression": "zstd"}

    with open(conffile, 'w') as file:
        config.write(file)

