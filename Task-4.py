#Example of Variables,Expression,Condition and function in python:
# Variables:
a = 3 # Assigning the value 3 to the variable a
b = "hello" # Assigning a string to the variable b
print(a)
print(b)
# Expression:
i = 2
j = 3
k = i + j # Adding value of variable i into the value of variable j
print (k)
d = i * j # multiply value of variable i into the value of variable j
print (d)

# Condition
n = 3
o = 9
if n>o:
	print ("n is greater than o")
elif o!=n:
	print ("o is not equal to n")
else:
	print ("condition false")

# function:
# Function for checking the equality
# and if and else statements
def chek_equality(m,g):
	if m == g:# Notice the indentation after function declaration
		print ("m is equal to g")
	else:
		print ("m is not equal to g")
#call the function and pass the value
chek_equality(11,11)

#Example of What is the maximum possible value of an integer in Python?
# Python 3 there is only one type : int

x = 10
print(type(x))# To chek the type of int

x = 10000000000000000000000000000000000000000000# To chek the type of long int
print(type(x))
# both different variable values gives the int type.
#here is the maximum possible value of an integer on your system by using sys.maxsize
import sys
l = sys.maxsize 
print(l)

#Example of Global and Local Variables in Python:
# Local Variable:
def student(x):
    s = "I am a student"  # This is a local variable
    print(s,x)

# Call the function with an argument
student("BSCS")

# Global Variable:
F = 50 #This is a global variable
def num():
    F = 30  # This is a local variable
    print(F) #its print the local variable

# Call the function 
num()
#
print(F)#its print the global variable

#Example of packing and unpackin:
#Unpacking:
def flu(a, b, c, d):# this function take 4 arguments
	print(a, b, c, d)

# call function
l = [1, 2, 3, 4]

# Unpacking l into four arguments
flu(*l)
#Another example unpacking
x = [1,5]
print(list(range(*x)))# here we un pakesd the list of x by using*

#Packing
def pack(*p):# all the elements which pass in call function is store here
    print()
pack(1,3,2,34)

#Example of Type conversion in python:
#Implicit Type conversion
x = 10  # Integer value
y = 2.5  # Float value
z = x + y  # Integer x is automatically converted to float Output=12.5 (a float)
print(z)  
#Another example of implicit
t = 5 + 6+7j #Adding the integer and complex number
print(t)# output is the complex 

#Explicit Type conversion
d = '10' # Integer value
s =int(d) # Manually convert in int
print(s)

#Another example of Explicit

v = "2" #string type
print(type(v)) #output string type
l = int(v) 
print(l) #output intiger type

#Example of Bytes object VS String in python
h = 'hello world'  # initialising a String
 
j = b'hello world' # initialising a byte object by using the b before string
print(h)
print(j)
print(type(h))
print(type(j))
# ENCODE
l = h.encode("ASCII")
print(l)
#DECODE
l = j.decode("ASCII")
print(l)

#Example of Print single and and multiple variable:
#Print single variable:
name = "Maryam"
print(name) #print the single variable by passing the single argument

#Print multiple variable:
age = 20
CGPA = 3.3
print(age,CGPA) #print the multiple variable by passing the single argument

#Example swap variable:
a = 3
b = 5
# By using arithmetic opretor
a = a + b #8
b = a - b #3
a = a - b #5
print(a)
print(b)
#By using temp
temp = a #3
a = b #5
b = temp #3

print(b)
print(a)
#By using ^
a = a ^ b
b = a ^ b
a = a ^ b
print(a,b)

#Example of Private variables

class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def display_info(self):
        print(f"The name is {self.__name} and the age is {self.__age}")

# Create an instance of the Student class
student = Student("MARAM", 20)
student.display_info()  # Corrected the method name to "display_info"

#Example of  Name(A special variable)in python:
if __name__ == "__main__":
    # Code here will run when the script is executed directly
    print("This script is the main program.")








