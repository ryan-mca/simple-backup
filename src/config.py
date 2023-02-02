import configparser
from os import mkdir
from os.path import exists

def parse_configs(conffile):
    config = configparser.ConfigParser()

    config.read(conffile)

    comp_method = config["Config"]["Compression"]

    return comp_method

def set_default_config(confdir, conffile):
    config = configparser.ConfigParser()

    if not exists(confdir):
        mkdir(confdir)

    if not exists(conffile):
        config["Config"] = {"Compression": "zstd"}

    with open(conffile, 'w') as file:
        config.write(file)

