#
# Example file for working with Calendars
#

# import the calendar module
import calendar
# Syntax: formatmonth(year, month, width=0, lines=0)

# Parameter:
# year: year of the calendar
# month: month of the calendar
# width: [optional] Specifies the width of the date columns, which are centered
# line: [optional] Specifies the number of lines that each week will use.

# create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)      #this tells what day to of the week. this case it starts with sunday, not monday
st = c.formatmonth(2020, 1)
# print(st)

# create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
st = hc.formatmonth(2020, 12)
# print(st)

# loop over the days of a month
# zeroes, in the answer, mean that the day of the week is in an overlapping month
# for i in c.itermonthdays(2020, 12):
    # print(i)
  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
# for name in calendar.month_name:
#     print(name)
# for day in calendar.day_name:
#     print(day)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print("Team meetings will be on: ")
for m in range(1,13):       #since 13 is not inclusive it will return 1-12 which are the months we need. 
    cal = calendar.monthcalendar(2020, m) # creates an array of weeks that represents each one of the month. m is the month number.
    weekone = cal[0]
    weektwo = cal[1]

    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else: 
        meetday = weektwo[calendar.FRIDAY]
    print("%10s %2d" % (calendar.month_name[m], meetday))
    
