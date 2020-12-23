#
# Example file for working with os.path module
#
import os #This module gives us the ability to work with Operating System related features.
# from os import path   # importing the Path module from the OS class here. if you don't import it you have to call os.path
import datetime # importing all modules from the datetime class.
from datetime import date, time, timedelta # importing date, time and timedelta modules from datetime class.
import time


def main():
  # Print the name of the OS
  # print(os.name)
  
  # Check for item existence and type
  # print("Item exists: " + str(os.path.exists("textfile.txt")))     # You notice I don't need to give it any path information because it's in the same directory as the script that's being run. otherwise i would.
  # print("Item is a file: " +str(os.path.isfile("textfile.txt")))
  # print("Item is a directory: " +str(os.path.isdir("textfile.txt")))

  # Work with file paths
  # print ("Item's path: " + str(os.path.realpath("textfile.txt")))
  # print ("Item's path and name: " + str(os.path.split(os.path.realpath("textfile.txt"))))
  
  # Get the modification time
  t = time.ctime(os.path.getmtime("textfile.txt"))
  # print (t)
  #basically two different ways of doing the same thing, just formatting it differently.
  # print (datetime.datetime.fromtimestamp(os.path.getmtime("textfile.txt")))
  
  # Calculate how long ago the item was modified
  td = datetime.datetime.now() - datetime.datetime.fromtimestamp(os.path.getmtime("textfile.txt"))
  print("It has been " + str(td) + " since the file was modified")
  print("Or, " + str(td.total_seconds()) + " seconds" )
  
if __name__ == "__main__":
  main()
