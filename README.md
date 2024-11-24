# pyshuffle
Simple script to shuffle files (mp3) in a directory, so dump players play the list random. The trick is sort the
files by names, starting by numbers, so we can "shuffle" then. Don't modify the name of the file, just add a 
mark in the begining so it becomes sorted.

## Usage (dry run)

```
python3.10 pyshuffle.py -d -v /Volumes/1TBSATA/mp3
```

## Usage (renamer)

```
python3.10 pyshuffle.py -v /Volumes/1TBSATA/mp3
```