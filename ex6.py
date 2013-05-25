# LPTHW ex6.py
# Written by jtbelles 5/21/13

# Setting variables
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# Printing variable 'x' and 'y'
print x
print y

# Printing strings with the variable 'x' and 'y' included
print "I said: %r." % x
print "I also said: '%s'." % y

# Setting variables
hilarious = True
joke_evaluation = "Isn't that joke so funny?! %r"

# Printing concantenation of the previous variables
print joke_evaluation % hilarious

# Setting variables for 'w' and 'e'
w = "This is the left side of..."
e = "a string with a right side."

# Printing concantenation of the previous variables
print w + e

