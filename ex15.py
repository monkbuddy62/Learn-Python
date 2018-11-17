# from package sys, lets use the argv module
#####from sys import argv
#script and filename will be our variable created from the command line arguments
#####script, filename = argv
#txt will be our variable, lets fill it with the output from the open function, opening the filename stored in the variable 'filename'
#####txt = open(filename)
#print a string with the raw data string thing and then saying what the filename is
#####print "YO, here's your file %r:" % filename
# the contents of the txt variable is now the object that is our file, to print that objects contents we print txt.read() ?? i dunno sure...
#####print txt.read()
# printing
print "HEY SLUMDOG, WHAT FILE YOU WANNA OPEN:"
# creating a var file_again letting its contents be some raw input from the user using a special > prompt
file_again = raw_input("> ")
# creating a variable called txt_again, and opening the filename thats stored in the variable file_again
txt_bitch = open(file_again)
#printing the contents of the file using .read()
print txt_bitch.read()
