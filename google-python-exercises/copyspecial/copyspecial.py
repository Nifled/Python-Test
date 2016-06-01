#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def getSpecialPaths(directory):
  filenames = os.listdir(directory)

  paths = []
  for filename in filenames:
    path = os.path.join(directory, filename)

    specialMatch = re.search(r'__\w+__', filename)
    if specialMatch:
      paths.append(path)
  return paths # returns list of strings containing special paths



def toDir(newDirName):
  newDir = directory + newDirName
  if os.path.exists(newDir):
    print('That path already exists fucboi')
    return
  os.mkdir(newDir)

  for filename in getSpecialPaths(directory):
    shutil.copy(filename, newDir)



def toZip(zipName):
  zipDir = directory + zipName
  # ----------------------------------
  if os.path.exists(zipDir):
    print('That path already exists fucboi')
    return
  os.mkdir(zipDir)
  for filename in getSpecialPaths(directory):
    shutil.copy(filename, zipDir)
  #------------------------------------
  # copied code from other method I wasn't able to avoid from writing
  shutil.make_archive(zipDir, 'zip', zipDir)
  shutil.rmtree(zipDir)


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    toDir(todir)
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    toZip(tozip)
    del args[0:2]

  if len(args) == 0:
    print("error: must specify one or more dirs")
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
