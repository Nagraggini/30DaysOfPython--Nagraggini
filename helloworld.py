'''
Number
Integer: Integer(negative, zero and positive) numbers Example: ... -3, -2, -1, 0, 1, 2, 3 ...
Float: Decimal number Example ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...
Complex Example 1 + j, 2 + 4j
String
A collection of one or more characters under a single or double quote. 
If a string is more than one sentence then we use a triple quote.
'''
print('Let\'s learn!')

username = input('Enter your name: ')
print(username)

age = int(input('What is your age? ')) #Marad a szám formátumban.
print(age)

#Pitagorasz-tétel
a= int(input('a:'))
b=int(input('b:'))
print('c')
print((a*2+b*2)**(0.5))

#coin flip💖
import random

num = random.randint(0, 1)   # Generates a random number that's either 0 or 1
result=0

if num > 0.5:
  result=result+1
  print('Heads')
else:
  print('Tails')