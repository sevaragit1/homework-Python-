#Number Data Type
#1
#n = float(input("Pleae enter the decimal number: "))
#print("The number is rounded to 2 decimal places: ", round(n, 2))

#2
#a = float(input("Please enter the number 1: "))
#b = float(input("Please enter the number 2: "))
#c = float(input("Please enter the number 3: "))
#largest = max(a, b, c) 
#smallest = min(a, b, c)
#print("Maximum: ", largest)
#print("Minimum: ", smallest)

#3
#km = float(input("Please enter the distance in kilometers: "))
#m = km/1000
#cm = km/100000
#print(f"The distance in meters is {m} and the distance in centimeters is {cm} ")

#4
#a = int(input("Please enter the number 1: "))
#b = int(input("Please enter the number 2: "))
#result = a // b
#remainder = a % b
#print("Result: ", result)
#print("Remainder: ", remainder)

#5
# celsius = float(input("Please enter the temperature in Celsius: ")) 
# fahrenheit = (Celsius * 9 / 5) + 32 
# print(f" Fahrenheit: {fahrenheit}") 

#6
#def last_digit(num):
    #return abs(num) % 10
#n = int(input("Please enter a number: "))
#print("The last digit is: ", last_digit(n))

#7
#def check_even_odd(num):
    #if num % 2 == 0:
        #return "Even"
    #else:
        #return "Odd"
#n = int(input("Please enter a number: "))
#print(f"The number {n} is {check_even_odd(n)}.")

#8
#def swap_values(a, b):
    #a, b = b, a
    #return a, b
#x = input("Enter the first value: ")
#y = input("Enter the second value: ")
#x, y = swap_values(x, y)
#print(f"After swapping: First value = {x}, Second value = {y}")


#String Data Type

#1
#s = input("Please enter a sentence: ")
#print("Capitalized sentence:", s.title())

#text = input("Please enter a string: ")
#v = "aeiouAEIOU"
#result = ''.join([char for char in text if char not in v])
#print("String without vowels:", result)

#3
#s = input("Please enter a string: ")
#print("Reversed string:", s[::-1])

#4
#text = input("Please enter a string: ")
#print("String with spaces replaced by underscores:", text.replace(" ", "_"))


#5
#w = input("Please enter a word: ")
#if w == w[::-1]:
    #print("The word is a palindrome.")
#else:
    #print("The word is not a palindrome.")

#6
#text = input("Enter teh text: ")
#for b in "a":
    #text = text.replace(b, "o")
#print(text)

#7
#e = input("Enter your email: ")
#u = email.split('@')[0]
#print("Username:", u)

#8
#text = input("Enter the string: ")
#title = text.title()
#print("Output:", title)

#9
#text = input("Enter the text: ")
#title = text[1:-1]
#print("Output:", title)

#10
#text = input("Enter the sentence: ")
#word = input("Enter the word: ")
#if word in text:
    #print("It is in the text")
#else:
    #print("It is not in the text")

#11
#text = input("Enter the text: ")

#find = input("Enter a character to find: ")

#position = text.find(find)

#if position != -1:
    #print(f"The first occurrence of '{find}' is at position: {position}")
#else:
    #print(f"'{find}' is not found in the string.")

#12
#string = "hello"
#print(string[-3:])

#13
#text, times = "hello", 3
#print(text * times)  

#14
#s = "This is a test"
#for word in s.split():
    #print(word)  

#15
#str = "hello"
#print(str[1::2])

#16
#str = "<String>"
#print(f"Title: {str}")

#17
#s = "hello world"
#print(s[::-1])

#18
#string1, string2 = "hello", "world!"
#print((len(string1) - len(string2)))



#Boolean Data Type

#1
#username = input("Please enter username: ")
#password = input("Please enter password: ")
#if username and password:
    #print("Both username and password are provided.")
#else:
    #print("One or both fields are empty.")


#2
#num1 = float(input("Please enter the first number: "))
#num2 = float(input("Please enter the second number: "))
#if num1 == num2:
    #print("The given numbers are equal.")
#else:
    #print("The given numbers are not equal.")

#3
#number = int(input("Please enter a number: "))
#print("The number is positive and even:", number > 0 and number % 2 == 0)

#4
#num1 = int(input("Please enter the first number: "))
#num2 = int(input("Please enter the second number: "))
#num3 = int(input("Please enter the third number: "))
#print("All numbers are different:", num1 != num2 and num1 != num3 and num2 != num3)

#5
#string1 = input("Enter first string: ")
#string2 = input("Enter second string: ")
#print("Same length:", len(string1) == len(string2))

#6
#number = int(input("Please enter a number: "))
#print("Divisible by both 3 and 5:", number % 3 == 0 and number % 5 == 0)

#7
#num1 = int(input("Please enter first number: "))
#num2 = int(input("Please enter second number: "))
#print("Sum > 50:", (num1 + num2) > 50)

#8
#number = int(input("Please enter a number: "))
#print("Between 10 and 20:", 10 <= number <= 20)
#key = (1,2,3)
#for k in key:
    #print(k**2)


