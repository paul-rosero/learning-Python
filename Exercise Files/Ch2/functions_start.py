#
# Example file for working with functions
#

# define a basic function
#functions are objects that can be passed around to other pieces of python code. 
def func1():            # the, : ,is scope definer
    print("I am a function")

#func1()           # returns or prints "I am a function" only since thats what is what the function does. 

#print(func1())          # prints  "I am a function" first since thats what the func1 does, the the outer print() executes and since the func1 does not return a value, python evaluates the return value to be the constant of none and prints the string representation of none.

#print(func1)            # this just prints the value of the function definition itself, which evaluates to: <function func1 at 0x7f89a8572ee0>

# function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)

# function that returns a value
def cube(x):
    return x * x * x

# function with default value for an argument


#function with variable number of arguments


