from sys import argv

script, filename = argv

print "Howdy, lets take a minute here and think about what were about to do"
print "I want to show you the contents of the file that you requested"

thatfile = open(filename)
print "here's your fucking shit:\n"
print thatfile.read()

print "\n\n\n"

print "...bitch"

