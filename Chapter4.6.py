##################
# Exercise 4.6
#
# New Instructions
# Rewrite your pay computation with time-and-a-half for overtime and create
# a function called computepay which takes two parameters (hours and rate)
# Enter Hours: 15
# Enter Rate: 10
# Pay: 475.0
#
## Old Instructions
## Rewrite your pay program using try and except so that your program handles
## non-numeric input gracefully by printing a message and exiting the
## program. The following shows two executions of the program: 
##
##  Enter Hours: 20
##  Enter Rate: nine
##  Error, please enter numeric input
##
##  Enter Hours: forty
##  Error, please enter numeric input
##  Enter Hours: 20
##################

error_msg_numeric = "Error, please enter numeric input"
def computepay(hour_in, rate_in):
  hours = hour_in
  try:
    float(hours)>=0
  except:
    print (error_msg_numeric)
    # ideally you would want this whole "check for valid input" 
    # in a while loop. This is a beginner's course, so here is a 
    # get-out-of-jail-free implementation.

  rate = rate_in
  try:
    float(rate) >=0
  except:
    print (error_msg_numeric)

  hours = float(hours)
  rate = float(rate)

  if hours > 40:
    extra_time = hours - 40
  else:
    extra_time = 0

  extra_pay = 0.5 * rate * extra_time

  pay = hours * rate + extra_pay

  print ('Pay: '),
  print pay

computepay(45,10)
