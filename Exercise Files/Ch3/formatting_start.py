#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined string
  # control codes 
  now = datetime.now()
  
  
  #### Date Formatting ####
  
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
  #print(now.strftime("The current year is: %Y, or for short: %y"))    # returns The current year is: 2020, or for short: 20
  #print(now.strftime("%a, %d, %b, %y"))   # returns Wed, 23, Dec, 20
  #print(now.strftime("%A, %D, %B, %Y"))   # returns Wednesday, 12/23/20, December, 2020
  
  # %c - locale's date and time, %x - locale's date, %X - locale's time
  # These control codes %c, %x, and %X allow you to use whatever the current locale's appropriate formatting is for dates and times.
  # print(now.strftime("Locale date and time: %c"))
  # print(now.strftime("Locale date: %x"))
  # print(now.strftime("Locale time: %X"))

  #### Time Formatting ####
  
  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
  print(now.strftime("Current time: %I:%M:%S %p"))
  print(now.strftime("24 time: %H:%M:%S"))

if __name__ == "__main__":
  main();
