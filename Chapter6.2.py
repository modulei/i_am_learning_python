##############
#
# Exercise 6.2
#
# Given that fruit is a string, what does fruit[:] mean?
#
# Answer: fruit[:] is the whole string stored in the variable fruit
# .... this is because omission of the first index starts the slice 
# at the beginning and omission of the second index goes to the end
# of the string.
#
##############

fruit = 'banana'
print fruit[:]

