##!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# /////////////////////////////////////////////////////////////////////////////
# //
# // pyshuffle.py 
# //
# // Simple script to shuffle files (mp3) in a directory, 
# // so dump players play the list random.
# //
# // 24/11/2024 15:50:06  
# // (c) 2024 Juan M. Casillas <juanm.casillas@gmail.com>
# //
# /////////////////////////////////////////////////////////////////////////////

import argparse
import re
import os
import os.path
import random
import sys

class Shuffler:
    def __init__(self, directory, verbose=False, dry_run=False):
        self.directory = directory
        if self.directory.endswith("/"):
            self.directory = self.directory[:-1]

        self.verbose = verbose
        self.dry_run = dry_run
        self.prefix = " --s-- "
        self.reprefix = "[0]+\d+%s"
        random.seed()

    def shuffle(self):

        counter = 0
        file_list = {}

        if not os.path.exists(self.directory):
            raise ValueError("directory %s doesn't exists. Bailing out" % self.directory)

        for dirpath, dirnames, filenames in os.walk(self.directory):
            for f in filenames:
                file_list[counter] = f
                counter +=1
        
        # shuffle
        if self.verbose and self.dry_run:
            print("dry run selected. No files will be renamed")

        keys = list(file_list.items())
        random.shuffle(keys)
        file_list = dict(keys)
        index = 0
        for i in file_list.keys():
        
            fname = file_list[i]
            source = "%s/%s" % (self.directory,fname)
            tgt = "%s/%010d%s%s" % (self.directory, index, self.prefix, file_list[i])

            if re.match(self.reprefix  % self.prefix, fname):
                # found previous mark, so rename it clearing it before, 
                # so the file name doesn't grow.
                fname = re.sub(self.reprefix  % self.prefix,"",fname)
                tgt = "%s/%010d%s%s" % (self.directory, index, self.prefix, fname)

            if self.verbose:
                print("[R]: %s -> %s" % (source, tgt))
            
            if not self.dry_run:
                if not os.path.exists(tgt):
                    os.rename(source, tgt)
                elif source == tgt:
                    pass
                else:
                    raise ValueError("file %s already exists. Bailing out" % tgt)
            index += 1
            
        if self.verbose:
            print("%d files processed" % len(keys))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dry-run", 
                        help="Show what we are going to do, but don't do it", 
                        action="store_true", 
                        default=False)
    parser.add_argument("-v", "--verbose", 
                        help="Show data about file and processing", 
                        action="count", 
                        default=0)
    parser.add_argument("input_directory", help="Directory to shuffle")
    args = parser.parse_args()

    shuffler = Shuffler(args.input_directory, args.verbose, args.dry_run)
    shuffler.shuffle()