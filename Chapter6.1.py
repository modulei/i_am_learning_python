#####################
# Exercise 6.1
#
# Write a while loop that starts at the last character in the string
# and works it way backwards to the first character in the string,
# printing each letter on a separate line, except backwards.
#
#####################

fruit = 'jerkface'
index = len(fruit)-1
i = 0

while i < len(fruit):
  letter = fruit[index]
  print letter
  index -= 1
  i += 1


