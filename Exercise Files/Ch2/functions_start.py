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
def power(num, x = 1):
    result = 1
    for i in range(x): #we will talk about loops later in the course.
        result = result * num 
    return result
#print(power(2))             #since we call default value of x=1 so it works normal.

#print(power(2,3))           #we override the default value of x when supplied with second argument.

#print(power(x=3, num=2))            # python3 lets you call functions with their named parameters along with their values, python interpreter figures out which argument to supply the values to, we don't have the call the function the arg in a particular order if you simply supply the names along with the values

#function with variable number of arguments


