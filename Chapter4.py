############
# Exercise 4.1
###########
import random

for i in range(10):
  x = random.random()
  print x


############
# Exercise 4.2
############

def print_lyrics():
  print "I'm a umberjack, and I'm okay."
  print 'I sleep all night and I work all day.'

def repeat_lyrics():
  print_lyrics()
  print_lyrics()

repeat_lyrics

###########
# Exercise 4.3
###########

def repeat_lyrics():
  print_lyrics
  print_lyrics

def print_lyrics():
  print "I'm a lumberjack, and I'm okay."
  print 'I sleep all night and I work all day.'

repeat_lyrics

##########
# Exercise 4.4
##########
# The purpose of the def keyword in Python is to indicate the start of a function and that that indented section of code is to be stored for later.

#########
# Exercise 4.5
#########
# Will print "ABC Zap ABC"
def fred():
  print "Zap"

def jane():
  print "ABC"

jane()
fred()
jane()


