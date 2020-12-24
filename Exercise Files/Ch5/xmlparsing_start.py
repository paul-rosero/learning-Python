# 
# Example file for parsing and processing XML
#
# Show to use the XML miniDOM class that Python provides, to load an XML file and then operate on the document while it's in memory.
import xml.dom.minidom        #first thing is import the module that lets you operate on an XML DOM.

def main():
  # use the parse() function to load and parse an XML file
  doc = xml.dom.minidom.parse("samplexml.xml")    #if path file is not in the same as here, you need to do path modifications like ./src/ that kind of manipulations. 
  
  # print out the document node and the name of the first child tag
  # If these property names don't look familiar to you, they are standard names that are used in the document object model, things like nodeName and firstChild and tagName.
  print(doc.nodeName)
  print(doc.firstChild.tagName)
  
  # get a list of XML tags from the document and print each one
  skills = doc.getElementsByTagName("skill")
  print("%d skills: " % skills.length)
  for skill in skills:
    print(skill.getAttribute("name"))
  
  # create a new XML tag and add it into the document
  newSkill = doc.createElement("skill")
  newSkill.setAttribute("name", "jQuery")
  doc.firstChild.appendChild(newSkill)
  
  skills = doc.getElementsByTagName("skill")
  print("%d skills: " % skills.length)
  for skill in skills:
    print(skill.getAttribute("name"))

if __name__ == "__main__":
  main();

