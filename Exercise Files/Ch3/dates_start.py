#
# Example file for working with date information
# Im telling the Python interpreter that from the "datetime" standard module that comes with the standard library, I want to import the "date", "time", and "datetime" classes.
from datetime import date
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  #print( "Today's date is ", today)

  # print out the date's individual components
  #print("Date components: ", today.month, today.day, today.year)
  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  #print("Today's weekday # is: ", today.weekday())
  days = ["mon", "tues", "wed", "thur", "fri", "sat", "sun"]
  #print("which is a: ", days[today.weekday()])
  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  today = datetime.now()
  print("The current date and time is: ", today)
  
  # Get the current time
  t = datetime.time(datetime.now())
  print(t)
 

  
if __name__ == "__main__":
  main();
  