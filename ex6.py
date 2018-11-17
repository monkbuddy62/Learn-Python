# declaring what x is, its a string that has the decimal 10 put into it
x = "There are %d types of people." % 10
# declaring that the variable binary
binary = "binary"
# declaring that the variable do_not contains the string "dont"
do_not = "don't"
# declaring that the variable y contains a string, also the variables binary and do_not are being called in it
y = "Those who know %s and those who %s. " % (binary, do_not)

# printing x
print x
# printing y
print y

# printing a string including all the RAW data of the variable....?
print "I said: %r." % x
# printing a string with the variabl y in it
print "I also said: '%s'." % y

# declaring that the variable hilarious is False
hilarious = False

# declaring that the variable joke_evaluation is a string with the 'r' conditional formatting thing after it
joke_evaluation = "Isn't that joke so funny?! %r"

# printing the previous sentance and injecting the variable hilarious into the end of it
print joke_evaluation % hilarious

#declaring 2 variables as strings
w = "This is the left side of..."
e = "a string with a right side."

#printing one then the other
print w + e
