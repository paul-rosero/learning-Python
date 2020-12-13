# 
# Example file for variables
#

# Declare a variable and initialize it
f= 0 #creating a variable named "f" and setting equal to 0
print(f) #printing this variable.

# re-declaring the variable works
f= "abc" #we are re-declaring it again with this line.
print(f)

# ERROR: variables of different types cannot be combined
#print("this is a string" + 123) 
        # in JavaScript this works, because JS does adds two different types, Python does not. This brings a TypeError: cannot concatenate 'str' and 'int' objects
print("this is a string" + str(123)) # the str() function changes anything to a string. 

# Global vs. local variables in functions
g= "im outside someFunction" #wrote a variable.
def someFunction() : #wrote a function that has the same local variable. 
    g="someFunction variable g" #this a local variable inside the function.
    print(g)

someFunction() #here we call the function to execute
print(g) #here we print what ever g is
