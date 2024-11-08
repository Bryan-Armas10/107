def comment_divisionn():
    print("=======================")

name = "leo"
last_name = "miranda"
cohort = 52
is_activve = True

print(name + " " + last_name + " #" + str(cohort))

integer = 10 # integer
float_num = 3.14 # float
text = "Hello" # string
is_sunny = False # bolean

comment_divisionn()
# ===== Type convversion =====
num = 9.75
print(int(num)) # convert a float  to an integer

age = 25
print(str(age)) # convert an integer to a strinng 

price = "19.99"
print(float(price)) # convert a string  to a float, Output: 19.99

comment_divisionn()
# challenge 
# create some variable called: name,, last_name, age and show them in a print
# "Hello, <name> <last_name>,, you are <age> years old."name = "Leo"\
name = "peter"
last_name = "parker"
age = 30
print(f"Hello, {name} {last_name}, you are {str(age)} years old.")

comment_divisionn()
# ===== Operators =====
x = 5
y = 3

print(x + y) # addition
print(x - y) # substraction
print(x * y) # multiplication
print(x / y) # division
print(x % y) # modulus 
print(x ** y) # exponentiation

comment_divisionn()
# Comparison Opperators
a = 10
b = 5

print(a == b) # equal to
print(a != b) # not equal to
print(a > b) # greater than
print(a < b) # less than
print(a >= b) # greater than or equal to
print(a <= b) # less than or equal to

x = 5
y = 10
print(x > 3 and y < 15) # True, because both condition are true
print(x > 3 or y > 15) # True, because at least one condition is true
print(not (x > 3)) # False,, because x is greater than 3 and we are applying not

comment_divisionn()
# =====Lists =====
fruits = ["apple", "banana", "cherry", "watermelonn"]
print(fruits) # acces de first element
print(fruits[0]) # accessing the first item
print(fruits[-1]) # accessing the last item

comment_divisionn()
# list methods
fruits.append("grape") # adds "orange" to the list 
print(fruits)

fruits.remove("banana") # removes "banana"
print(fruits)

print(fruits.pop(1)) # removes and prints item at index 1 "cherry"
print(fruits)

print(fruits.index("grape")) # returns index of "grape"

fruits.append("apple")
print(fruits) # returns the number of times "apple" appears in the 
print(fruits.count("apple")) # returns hoy many times "apple" appears

comment_divisionn()
# ===== if statements =====
age = 10

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

x = 10

if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is less than 10")


comment_divisionn()
# ===== for loopps =====
for i in range(5): # loop from 0 to 4
    print(i) 

fruits = ["apple","banana","chherry"] # fruit list

for x in fruits:
    print(f"fruit: {x}")

comment_divisionn()
# ===== Functions =====
def greet():
    print("Hello from greet function")
greet() # calls the function

def say_hi(name): # parameter
    print("Hi, " + name)

say_hi("Bruce") # argument