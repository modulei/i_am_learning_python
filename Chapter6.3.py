##############
# Exercise 6.3
# Encapsulate this code in a function named count, and generalize it so that it
# accepts the string and the letter as arguments.
#
# word = 'banana'
# count = 0
# for letter in word:
#   if letter == 'a':
#     count = count + 1
# print count
##############

word = 'banana'
letter = 'a'

def count(my_word, my_letter):
  count = 0
  for letter in word:
    if letter == my_letter:
      count = count + 1
  print count

count(word,letter)
