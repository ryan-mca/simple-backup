import csv
from os.path import exists
from os import mkdir
import datetime

def write_default(dir: str, csvfile: str):
    """Creates a default CSV file

    Args:
        dir (str): Path to the config dir
        csvfile (str): Path to the CSV file
    """
    # Checks if the dir exists, if not it creates it
    if not exists(dir):
        mkdir(dir)

    # Checks if the CSV file exists and creates a basic one if not
    if not exists(csvfile):
        with open(csvfile, "w") as file:
            headers = ["filename", "date_created"]
            writer = csv.DictWriter(file, headers)
            writer.writeheader()

def update_backups(days: int):
    