# simple-backup
A simple script to backup files

## Compression methods

Currently supports the following

* ZSTD
* ZIP
* BZIP
* XZ
* GZIP
* LZ4
* TAR
* None

## Usage
~~~bash
.py INFILE OUTFILE -c | --compression COMPRESSION_METHOD # Optional
~~~

## WIP

Currently working on automatically managing backup files. EG. deleting old backups after a week

Also working on packaging