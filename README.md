# pyshuffle
Simple script to shuffle files (mp3) in a directory, so dump players play the list random. The trick is sort the
files by names, starting by numbers, so we can "shuffle" then. Don't modify the name of the file, just add a 
mark in the begining so it becomes sorted. Only renames files with "music" extensions:

```
    extensions = [  ".3gp",     ".aa",      ".aac",     ".aax",
                    ".act",     ".aiff",    ".alac",    ".amr",
                    ".ape",     ".au",      ".awb",     ".dss",
                    ".dvf",     ".flac",    ".gsm",     ".iklax",
                    ".ivs",     ".m4a",     ".m4b",     ".m4p",
                    ".mmf",     ".movpkg",  ".mp3",     ".mpc",
                    ".msv",     ".nmf",     ".ogg",     ".oga",
                    ".mogg",    ".opus",    ".ra",      ".rm",
                    ".raw",     ".rf64",    ".sln",     ".tta",
                    ".voc",     ".vox",     ".wav",     ".wma",
                    ".wv",      ".webm",    ".8svx",    ".cda"
    ]
```

## Usage (dry run)

```
python3.10 pyshuffle.py -d -v /Volumes/1TBSATA/mp3
```

## Usage (renamer)

```
python3.10 pyshuffle.py -v /Volumes/1TBSATA/mp3
```