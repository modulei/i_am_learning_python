##################
# Exercise 4.7
# New Instructions
# Rewrite the grade program from the previous chapter using a function called
# computegrade that takes a score as its parameters and returns a grade as
# a string.
#
## Old Instructions
## Write a program to prompt for a score between 0.0 and 1.0. If the
## score is out of range print an error. If the score is between 0.0 and 1.0, print a
## grade using the following table:
##  Score Grade
##  >= 0.9 A
##  >= 0.8 B
##  >= 0.7 C
##  >= 0.6 D
##   < 0.6 F
##
# Missing: Error looping.
##################

error_msg_invalid = "ERROR: Invalid input."

def computegrade(score):
  score = float(score)
  if score < 0.6:
    print ('F')
    #break
  elif score >= 0.9:
    print ('A')
    #break
  elif score >= 0.8:
    print ('B')
    #break
  elif score >= 0.7:
    print('C')
    #break
  elif score >= 0.6:
    print('D')
    #break
  else:
    print ('wtf?')

input_score = raw_input('Enter a score between 0.0 and 1.0: ')
try:
  if (float(input_score) >= 0) and ( float(input_score) <= 1 ):
    computegrade(input_score)
    #print('valid input, thanks!')
  else:
    print (error_msg_invalid)
  #input_score = raw_input('Enter a score between 0.0 and 1.0: ')
except:
  print (error_msg_invalid)
  #input_score = raw_input('Enter a score between 0.0 and 1.0: ')
