# LPTHW ex5.py

name = 'Bob C. Frank'
age = 29 # not a lie
height = 72 # inches
m_height = height * 2.54
weight = 180 # pounds
m_weight = weight * 0.453592
eyes = 'Hazel'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's weighs %d pounds." % weight
print "Actually that's not to heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee intake." % teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

# Showing metric height and weight equivalents
print "If I were in Europe I would weigh %f kilos and be %f centimeters tall." % (m_weight, m_height)
