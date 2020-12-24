# 
# Example file for parsing and processing JSON
#
import urllib.request 
# In order to process JSON I have to import the correct module which is the JSON module.
import json

def printResults(data):
  # Use the json module to load the string data into a dictionary
  theJSON = json.loads(data)
  
  # now we can access the contents of the JSON like any other Python object
  if "title" in theJSON["metadata"]:
    print(theJSON["metadata"]["title"])
  
  # output the number of events, plus the magnitude and each event name  
  count = theJSON["metadata"]["count"]
  print(str(count) + " events recorded")
  
  # for each event, print the place where it occurred
  for i in theJSON["features"]:
    print(i["properties"]["place"])
  print("===========\n")

  # print the events that only have a magnitude greater than 4
  for i in theJSON["features"]:
    if i["properties"]["mag"] >= 4.0:
      print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])      # I'm going to use %2.1f. That formats a decimal with 2.1 spaces. So two significant digits and one decimal digit. So it prints 4.0 instead of just 4
  print("===========\n")
  # print only the events where at least 1 person reported feeling something
  for i in theJSON["features"]:
    if i["properties"]["felt"] != None:
      if i["properties"]["felt"] > 0:
        print("%2.1f" % i["properties"]["mag"], i["properties"]["place"], "reported " + str(i["properties"]["felt"]) + " times")
  

def main():
  # define a variable to hold the source URL
  # In this case we'll use the free data feed from the USGS
  # This feed lists all earthquakes for the last day larger than Mag 2.5
  urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

  # Open the URL and read the data
  webUrl = urllib.request.urlopen(urlData)
  print ("result code: " + str(webUrl.getcode()))    # this will retrieve the code to see if its a 200 or what ever else.
  if (webUrl.getcode() == 200):
    data = webUrl.read()
    printResults(data)
  else:
    print("Received error, can't parse results")
  

if __name__ == "__main__":
  main()
