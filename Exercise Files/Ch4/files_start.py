#
# Read and write files using the built-in Python file methods
#

def main():  
  # So to open a file, I call the open function and it takes two arguments. The first is the file to operate on, and the second argument is the kind of access that you want. 
  # Open a file for writing and create it if it doesn't exist
  # f = open("textfile.txt", "w+")    # So in this example, I'm opening "textfile.txt" for write access, because of the "w" parameter, and the plus sign means to create the file if it doesn't already exist. And when the function returns, I'm storing the creative file object in the "f" variable.
  
  # Open the file for appending text to the end
  # f = open("textfile.txt", "a")      # In this case, I'm going to pass a different mode to it, which is "a". So the "a" parameter means to append data to the end of the file instead of overwriting all the existing content that's already in there. The rest of the code will remain the same, which essentially means that 10 new lines will be added to the existing file. 

  # write some lines of data to the file
  # for i in range(10):
  #     f.write("This was line " + str(i) + "\r\n")
  
  # close the file when done, everytime you open a file you have to close it once you are done working inside that file. 
  # f.close()

  # Open the file back up and read the contents
  f = open("textfile.txt", "r")     # this makes the file readable when you open. There are 2 ways of doing this.
  #option1:
  # if f.mode == "r":
  #   contents = f.read() 
  #   print(contents)     # this reads the entire file, if file is too big it will long wait. 
  
  #option2:
  if f.mode == "r":
    fl = f.readlines()
    for x in fl:
      print(x)
    
if __name__ == "__main__":
  main()
