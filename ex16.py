#from package sys get argv up in here so we can grab arguments form the command line sucka!
from sys import argv
#the first bit might be mandatory, but the second bit is our variable
#AHA the first argument is always script name and it is also being counted in number of arguments this is just a thing that argv does.
script, filename = argv

# print a line and put the raw data that is the string 'filename'in too
print "We're going to erase %r." % filename
#print string
print "if you don't want that, hit CTRL-C (^C)."
#print a string
print "If you do want that, hit RETURN."
# have a ? cursor on the screen thats waiting for input any input
raw_input("?")

print "Opening the file..."
#make variable called target it is now a file with write pemrissions
target = open(filename, 'w')

#clears the contents of the file
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

#three strng inputs as new variables
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
#write the contents of each varianle and write a new line after
target.write("%r\n%r\n%r" % (line1, line2, line3))
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
#close the file
print "And finally, we close it."
target.close()
