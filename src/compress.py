import tarfile as tf
import lz4.block
import zstd
import zipfile
import shutil
from os.path import isdir
from os import mkdir, remove

COMP_METHODS = ["zstd", "zip", "gzip", "bzip", "xz", "lz4", "tar", "none"]
FILE_EXT = [".tar.zst", ".zip", ".tar.gz", ".tar.bz2", ".tar.xz", ".tar.lz4", ".tar"]


def compress(dest_file, orig_file, comp_method):
    try:
        if comp_method in COMP_METHODS:
            eval(f"create_{comp_method}(dest_file, orig_file)")
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

def create_tar(dest_file, orig_file):
    with tf.open(f"{dest_file}.tar", "w") as tar:
        tar.add(orig_file)

def create_gzip(dest_file, orig_file):
    with tf.open(f"{dest_file}.tar.gz", "w:gz") as tar:
        tar.add(orig_file)

def create_bzip(dest_file, orig_file):
    with tf.open(f"{dest_file}.tar.bz2", "w:bz2") as tar:
        tar.add(orig_file)

def create_xz(dest_file, orig_file):
    with tf.open(f"{dest_file}.tar.xz", "w:xz") as tar:
        tar.add(orig_file)

def create_zstd(dest_file, orig_file):
    with tf.open(f"{dest_file}.tar", "w") as tar:
        tar.add(orig_file)

    with open(f"{dest_file}.tar", "rb") as file:
        data = file.read()

    remove(f"{dest_file}.tar")
    compressed_data = zstd.compress(data)

    with open(f"{dest_file}.tar.zst", "wb") as file:
        file.write(compressed_data)

def create_lz4(dest_file, orig_file):
    with tf.open(f"{dest_file}.tar", "w") as tar:
        tar.add(orig_file)

    with open(f"{dest_file}.tar", "rb") as file:
        data = file.read()

    remove(f"{dest_file}.tar")
    compressed_data = lz4.block.compress(data)

    with open(f"{dest_file}.tar.lz4", "wb") as file:
        file.write(compressed_data)

def create_zip(dest_file, orig_file):
    with zipfile.ZipFile(f"{dest_file}.zip", "w") as zip:
        zip.write(orig_file)

def create_none(dest_file, orig_file):
    try:
        if isdir(orig_file):
            shutil.copytree(orig_file, dest_file)
        else:
            shutil.copy2(orig_file, dest_file)
    except shutil.SameFileError:
        exit("Files Must Have Different Names")