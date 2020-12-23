#
# Example file for working with classes

# wrote from here to create class
class myClass():
    def method1(self):          #this is a regular function but once it's inside a class its called a method.
        print("myClass method1")
    
    def method2(self, someString):          #self is written just like "this" in javascript to represent that specific method. 
        print("myClass method2 " + someString)
class anotherClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("anotherClass method1")
    
    def method2(self, someStrig):
        print ("anotherClass method2")

def main():
    c = myClass()           # we instantiate the class by calling it like this. it will instantiate an object instance of this class. Now we can call methods in the class like I can call methods on any other object. 
    c.method1()
    c.method2("this is a string")
    
    c2 = anotherClass()
    c2.method1()
    c2.method2("this is a sstring")
if __name__ == "__main__":
    main()
