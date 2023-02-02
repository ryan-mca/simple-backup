from shutil import make_archive
from os import remove

def create_zstd(dest_file: str, orig_file: str):
    """Creates a tarfile compressed with zstd

    Args:
        dest_file (str): The file to create
        orig_file (str): The original file / folder
    """
    import zstd

    # Creates a tar archive
    try:
        make_archive(dest_file, "tar", orig_file)

        # Opens the tar archive and then reads the data
        with open(f"{dest_file}.tar", 'rb') as file:
            data = file.read()

        # Compresses the data
        compressed_data = zstd.compress(data)

        # Writes the data
        with open(f"{dest_file}.tar.zst", 'wb') as file:
            file.write(compressed_data)

        # Removes the original tarfile
        remove(f"{dest_file}.tar")
    except FileNotFoundError:
        remove(f"{dest_file}.tar")
        exit("File Not Found")

def create_zip(dest_file: str, orig_file: str):
    """Creates a zip archive

    Args:
        dest_file (str): The file to create
        orig_file (str): The original file / folder
    """
    make_archive(dest_file, "zip", orig_file)


def create_gzip(dest_file: str, orig_file: str):
    """Creates a tarfile compressed gzip

    Args:
        dest_file (str): The file to create
        orig_file (str): The original file / folder
    """
    try:
        make_archive(dest_file, "gztar", orig_file)
    except FileNotFoundError:
        remove(f"{dest_file}.tar.gz")
        exit("File Not Found")

def create_xz(dest_file: str, orig_file: str):
    """Create a tarfile compressed with xz

    Args:
        dest_file (str): The file to create
        orig_file (str): The original file / folder
    """
    try:
        make_archive(dest_file, "xztar", orig_file)
    except FileNotFoundError:
        remove(f"{dest_file}.tar.xz")
        exit("File Not Found")

def create_bzip(dest_file: str, orig_file: str):
    """Creates a tarfile compressed with bzip

    Args:
        dest_file (str): The file to create
        orig_file (str): The original file / folder
    """
    try:
        make_archive(dest_file, "bztar", orig_file)
    except FileNotFoundError:
        remove(f"{dest_file}.tar.bz2")
        exit("File Not Found")

def create_lz4(dest_file: str, orig_file: str):
    """Creates a tarfile compressed with lz4

    Args:
        dest_file (str): The file to create
        orig_file (str): The original file / folder
    """
    import lz4.block

    try:
        # Creates a tar archive
        make_archive(dest_file, "tar", orig_file)

        # Reads the uncompresed data
        with open(f"{dest_file}.tar", "rb") as file:
            data = file.read()

        # Compresses the data
        compressed_data = lz4.block.compress(data)

        # Writes the compressed file
        with open(f"{dest_file}.tar.lz4", "wb") as file:
            file.write(compressed_data)

        # Removes the original tarfile
        remove(f"{dest_file}.tar")
    except FileNotFoundError:
        remove(f"{dest_file}.tar.lz4")
        exit("File Not Found")

def create_tar(dest_file: str, orig_file: str):
    """_summary_

    Args:
        dest_file (str): The file to create
        orig_file (str): The original file / folder
    """
    try:
        make_archive(dest_file, "tar", orig_file)
    except FileNotFoundError:
        remove(f"{dest_file}.tar")
        exit("File Not Found")

def copy(dest_file: str, orig_file: str):
    """Copies the file / folder

    Args:
        dest_file (str): The file / folder to create
        orig_file (str): The file / folder to copy
    """
    from shutil import copytree, copy2
    from os.path import isdir
    try:
        if isdir(orig_file):
            copytree(orig_file, dest_file)
        else:
            copy2(orig_file, dest_file)
    except FileExistsError:
        exit("File / folder exists")
    except FileNotFoundError:
        exit("File Not Found")