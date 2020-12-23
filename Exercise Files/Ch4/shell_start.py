#
# Example file for working with filesystem shell methods
#
# Python provides a set of utilities for manipulating files using the operating system's shell utilities.

import os.path
from os import close, path

# Need to import shutil to be able to use the shell utilities.
import shutil
# So in order to work with zip files, I'm going to use the shell utilities make archive function in order to create an archive file that contains the contents of this whole directory. And to do that, I need to import the make archive module.
from shutil import make_archive
from zipfile import ZipFile



def main():
  # make a duplicate of an existing file
  if path.exists("textfile.txt"):
  # if path.exists("texxtfile.txt"):    # this i created to check if a file is not there, to create it using the else statement at the end.
    # get the path to the file in the current directory
    src = path.realpath("textfile.txt")
    
    # let's make a backup copy by appending "bak" to the name
    dst = src + ".bak"
    
    # copy over the permissions, modification times, and other info
    # shutil.copy(src, dst)     # ONLY copies the content of the files. 
    # shutil.copystat(src, dst)       # if you want to copy everything else use this. 

    # rename the original file
    # os.rename("texxtfile.txt", "newfile.txt")
    
    # now put things into a ZIP archive
    # root_dir, tail = path.split(src)
    # shutil.make_archive("archive", "zip", root_dir)     #  archive.zip was created and right now this archive contains all the contents of this directory. That's what happens by default, but you have more control over what you add to it. 

    # more fine-grained control over ZIP files
    with ZipFile("testzip.zip", "w") as newzip:     # So this code creates a new zip file object named test zip and I'm using the W parameter to indicate that want to write to the file. The object I get back, I'm going to temporarily name my new zip variable. And then I can use that object to manipulate the data and write content to the file.
      newzip.write("textfile.txt")
      newzip.write("textfile.txt.bak")

  else:
    open("texxtfile.txt", "w")
    close("texxtfile.txt")

      
if __name__ == "__main__":
  main()
