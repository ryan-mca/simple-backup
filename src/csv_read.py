import csv
from os.path import exists
from os import mkdir
from datetime import date

TODAY = date.today()

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
            headers = ["filename", "date_created", "store_length"]
            writer = csv.DictWriter(file, headers)
            writer.writeheader()

def add_file(days: int, fname: str, csvfile: str):
    with open(csvfile, "a") as file:
        writer = csv.DictWriter(file)
        writer.writerow({"filename": fname,
                        "date_created": TODAY,
                        "store_length": days})

def update_files(csvfile: str):
    with open(csvfile, "r") as file:
        reader = csv.DictReader(file)

        csvlist = []

        for row in reader:
            csvlist.append(row)

    print(csvlist[1]["store_length"])