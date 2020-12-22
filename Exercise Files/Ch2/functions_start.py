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

#func2(10,20)            # returns or prints "10 20" only since thats what is what the function does.

#print(func2(10,20))            # prints  "10 20" first since thats what the func1 does, the the outer print() executes and since the func1 does not return a value, python evaluates the return value to be the constant of none and prints the string representation of none.

# function that returns a value
def cube(x):
    return x * x * x

#cube(3)            # does not print anything since it returns a value. so nothing shows but everything is working as it should 

#print(cube(3))            # this has a return a value, so that is what gets printed. since this has a return value. 
# function with default value for an argument


#function with variable number of arguments


