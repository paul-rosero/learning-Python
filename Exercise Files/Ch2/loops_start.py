#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
# while (x < 5):      #executes a block of code while a particular condition evaluates true
#   print(x) # while x is less than 5 it will print 
#   x = x + 1

  # define a for loop; these are iterators
# the range function will start with that 5 and iterate till but not including 10.
# for x in range(5,10):
#   print(x)

  # use a for loop over a collection
#days = ["Mon", "Tues", "Wed", "Thu", "Fri", "Sat", "Sun"]
#for day in days:      # here it iterates over array and prints out all the days in the array.
#  print(day)
  
  # use the break and continue statements
#for x in range(5, 10):       
#  if (x == 7): break      # break the execution of a loop if a condition is met. The break will cause this for loop to terminate and fall through to next block of code. in this case once it hits 7 it stops and no longer run. so it only prints 5,6.
#  if (x % 2 == 0): continue       #continue basically means skip the rest of the execution of this loop, and continue with the loop by going back up to the top of the loop. 
#  print(x) 

  #using the enumerate() function to get index in an array
days = ["Mon", "Tues", "Wed", "Thu", "Fri", "Sat", "Sun"]
for i, day in enumerate(days):     # enumerate funciton will iterate over this collection like a loop normally would, but in addition to retruning the value of the item being looked, it also returns a value that is the index of the item in question. it returns two values, index of the member of the collection that we're looking at, as well as the actual member of the collection. 
 print(i, day)
  
if __name__ == "__main__":
  main()
