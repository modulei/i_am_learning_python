##################
# Exercise 2.2
# Write a program that uses raw_input to prompt a user for their name and then
# welcomes them. 
#
# Enter your name: Chuck
# Hello Chuck
#

username = raw_input('Enter your name: ')
print ("Hello " + username)


###################
# Exercise 2.3
# Write a program to prompt the user for hours and rate per hour to compute
# gross pay.
#
# Enter Hours: 35
# Enter Rate: 2.75
# Pay: 96.25
#

hours = raw_input('Enter Hours: ')
rate = raw_input('Enter Rate: ')
pay = float(hours) * float(rate)
print ('Pay: '),
print pay


###################
# Exercise 2.4 
# Assume that we execute the following assignent statements:

width = 17
height = 12.0

# For each of the following expression, write the value of the expression and
# the type (of the value of the expression):
#
# 1. width/2
####  = 8    #int

print width/2
print type(width/2)

# 2. width/2.0
####  = 8.5  #float

print width/2.0
print type(width/2.0)

# 3. height/3
####  = 4.0  #float

print height/3
print type(height/3)

# 4. 1 + 2 * 5
#### = 11    #int

print 1 + 2 * 5
print type(1 + 2 * 5)


###################
# Exercise 2.5
# Write a program which prompts the user for a Celcius temperature, convert the
# temperature to Fahrenheit and print out the converted temperature.

temp_Celcius = raw_input('Enter a temperature in Celcius: ')
temp_Farenheight = (float(temp_Celcius) * 1.8) + 32
print ('This is equivalent to '),
print temp_Farenheight,
print (' degrees Farenheight')

