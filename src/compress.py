import tarfile as tf
import lz4.block
import zstd
import zipfile
import shutil
from os.path import isdir
from os import mkdir, remove

COMP_METHODS = ["zstd", "zip", "gzip", "bzip", "xz", "lz4", "tar", "none"]
FILE_EXT = [".tar.zst", ".zip", ".tar.gz", ".tar.bz2", ".tar.xz", ".tar.lz4", ".tar"]


def compress(dest_file: str, orig_file: str, comp_method: str):
    """Checks for the compression method and creates the right archive

    Args:
        dest_file (str): The file to write
        orig_file (str): The file to read
        comp_method (str): The compression method
    """
    try:
        if comp_method in COMP_METHODS:
            fname = eval(f"create_{comp_method}(dest_file, orig_file)")
        else:
            exit("Compression mode not supported")
    except FileNotFoundError:
        while True:
            try:
                for ext in FILE_EXT:
                    remove(f"{dest_file}{ext}")
            except FileNotFoundError:
                pass
            break
        exit("File Not Found")

    return fname

def create_tar(dest_file: str, orig_file: str):
    """Creates an uncompressed tarfile

    Args:
        dest_file (str): The file to write
        orig_file (str): the file to read
    """
    fname = dest_file + ".tar"
    with tf.open(fname, "w") as tar:
        tar.add(orig_file)
    return fname

def create_gzip(dest_file: str, orig_file: str):
    """Creates a tarfile compressed with gzip

    Args:
        dest_file (str): The file to write
        orig_file (str): The file to read
    """
    fname = dest_file + ".tar.gz"
    with tf.open(fname, "w:gz") as tar:
        tar.add(orig_file)
    return fname

def create_bzip(dest_file: str, orig_file: str):
    """Creates a tarfile compressed with bzip2

    Args:
        dest_file (str): The file to write
        orig_file (str): The file to read
    """
    fname = dest_file + ".tar.bz2"
    with tf.open(fname, "w:bz2") as tar:
        tar.add(orig_file)
    return fname

def create_xz(dest_file: str, orig_file: str):
    """Creates a tarfile compressed with xz / lzma

    Args:
        dest_file (str): The file to write
        orig_file (str): The file to read
    """
    fname = dest_file + ".tar.xz"
    with tf.open(fname, "w:xz") as tar:
        tar.add(orig_file)
    return fname

def create_zstd(dest_file: str, orig_file: str):
    """Creates a tarfile compressed with zstd

    Args:
        dest_file (str): The file to write
        orig_file (str): The file to read
    """
    fname = dest_file + ".tar.zst"
    with tf.open(f"{dest_file}.tar", "w") as tar:
        tar.add(orig_file)

    with open(f"{dest_file}.tar", "rb") as file:
        data = file.read()

    remove(f"{dest_file}.tar")
    compressed_data = zstd.compress(data)

    with open(fname, "wb") as file:
        file.write(compressed_data)

def create_lz4(dest_file: str, orig_file: str):
    """Creates a tarfile compressed with lz4

    Args:
        dest_file (str): The file to write
        orig_file (str): The file to read
    """
    fname = dest_file + ".tar.lz4"
    with tf.open(f"{dest_file}.tar", "w") as tar:
        tar.add(orig_file)

    with open(f"{dest_file}.tar", "rb") as file:
        data = file.read()

    remove(f"{dest_file}.tar")
    compressed_data = lz4.block.compress(data)

    with open(fname, "wb") as file:
        file.write(compressed_data)

def create_zip(dest_file: str, orig_file: str):
    """Creates a zipfile

    Args:
        dest_file (str): The file to write
        orig_file (str): The file to read
    """
    fname = dest_file + ".zip"
    with zipfile.ZipFile(fname, "w") as zip:
        zip.write(orig_file)

def create_none(dest_file: str, orig_file: str):
    """Copies the file to the destination

    Args:
        dest_file (str): The file to write
        orig_file (str): The file to read
    """
    try:
        if isdir(orig_file):
            shutil.copytree(orig_file, dest_file)
        else:
            shutil.copy2(orig_file, dest_file)
    except shutil.SameFileError:
        exit("Files Must Have Different Names")
    return dest_file