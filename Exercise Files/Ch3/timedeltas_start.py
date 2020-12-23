#
# Example file for working with timedelta objects
# A frustrating scenario involving dates and times, involves performing mathematical operations on dates and times themselves. So for example, given a particular date, you might want to calculate a date in the future or the past relative to that date. We can use the time delta class in Python to help us with this

from datetime import date
from datetime import time
from datetime import datetime
#add this code to be able to use timedelta
from datetime import timedelta
# A timedelta is basically a span of time. It's not a particular date, it's not a particular time, it's a span of time. And you can use this class to perform time-based mathematics.

# To construct a basic timedelta, all you need to do is create the timedelta class and pass in the amount of time that you want the timedelta to represent.
# print(timedelta(days=365, hours=5, minutes=1, seconds=23))

# print today's date
now = datetime.now()
print("Today is: " + str(now))

# print today's date one year from now
print("Two years from today will be: " + str(now + timedelta(days=730)))

# create a timedelta that uses more than one argument
print("In 2 days and 3 weeks it will be: " + str(now + timedelta(days=2, weeks=3)))

# calculate the date 1 week ago, formatted as a string


### How many days until April Fools' Day?


# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year


# Now calculate the amount of time until April Fool's Day  

