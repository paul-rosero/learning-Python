# 
# Example file for retrieving data from the internet
#
# In this first example, we're going to just retrieve data from a server and print the results. 
import urllib.request     # So in order to make a request to a web server, I need to import the urllib.request module. So I'll so that first. So this module provides the classes and code I need to make http requests. 

def main():
  webUrl = urllib.request.urlopen("http://www.google.com")      # Call the urlopen function on the request class, and that will give me back a response object. And url open just takes a string, represents the url.
  print("result code: " + str(webUrl.getcode()))      # And this will just be a regular http result code, so example: 200 if everything is okay, 404 if the file's not found.
  data = webUrl.read()
  print(data)     # I'm just reading the entire contents of this url into a variable named data, and then it's going to print it out. So if all goes well, this should be the html code for Google's homepage. 


if __name__ == "__main__":
  main()
