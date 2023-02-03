import csv
import datetime
from os.path import exists
from os import mkdir, remove, getcwd

TODAY = datetime.date.today()

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

def add_file(days = 7, fname = "", csvfile = ""):
    """Addes the given file to the csvfile

    Args:
        days (str): The amount of days to track files
        fname (str): The filename to add
        csvfile (str): The file to write to
    """
    if not fname.startswith("/"):
        fname = f"{getcwd()}/{fname.replace('./', '')}"

    with open(csvfile, "a") as file:
        writer = csv.DictWriter(file, ["filename", "date_created", "store_length"])
        writer.writeheader()
        writer.writerow({"filename": fname,
                        "date_created": TODAY,
                        "store_length": days})

def update_files(csvfile: str):
    with open(csvfile, "r") as file:
        reader = csv.DictReader(file)
        try:
            for row in reader:
                year, month, day = (row["date_created"].split("-"))
                created = datetime.date(int(year), int(month), int(day))
                day_diff = str(TODAY - created)
                if (day_diff[0:1].strip() >= row["store_length"]):
                    remove(row["filename"])
        except ValueError:
            pass