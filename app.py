# ~~~~~~~~~~~~BASICS~~~~~~~~~~~
# to run click on run or play symbol
# 'print' tells python what to show in console
# code is executed in order that it's written
print("Hello World")
# drawing a shape
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

# ~~~~Variables & Data Types~~~~~~~~~~~~
character_name = "John"
character_age = "50"
print("There once was a man named " + character_name + ",")
print("he was " + character_age + " years old.")
# updating variable inside of the program
character_name = "Mike"
print("He really liked the name " + character_name + ",")
print("but didn't like being " + character_age + ".")

# ~~~~~Working with Strings~~~~~
phrase = "Giraffe Academy"
# new line
print("Giraffe\nAcademy")
# quotations
print("Giraffe\"Academy\"")
# concatention using var
print(phrase + " is cool")
# FUNCTIONS
# lowercase
print(phrase.lower())
# uppercase
print(phrase.upper())
# boolean based on whether or not its upper cased
print(phrase.isupper())
# combo of functions
print(phrase.upper().isupper())
# length **VERY USEFUL**
print(len(phrase))
# singling out characters (index) ps indexing starts at 0 aka  first letter is position 0
print(phrase[3])
# index (passing a parameter)
print(phrase.index("e"))
# replace (changes first parameter for second)
print(phrase.replace("Giraffe", "Elephant"))

# ~~~Working with Numbers~~~~
print(3.05)
# basics add,multi,sub,div, order of operations, modulus(gives remainder)
print(5 + 7.89)
print(3 * 11)
print(5-6)
print(7/3)
print(3 * (6+9))
print(10 % 6)
my_num = 5
print(my_num)
# convert number to string NEED to convert numbers if u wanna use it next to a string
print(str(my_num) + " my fave number")
# FUNCTIONS
# abs - absolute value
print(abs(my_num))
# pow (number, power)
print(pow(3, 5))
# max -returns bigger number
print(max(234,234324))
# min
print (min(123,1.2))
# round
print(round(3.567))
# IMPORTING FROM MATH MODULE
from math import *
# round down
print(floor(3.7))
# round up
print(ceil(9.12))
# square root
print(sqrt(36))



