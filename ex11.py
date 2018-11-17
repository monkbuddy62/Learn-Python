#ask us how old we are then creates the variable age, that equals what we type in
print "How old are you?",
age = raw_input()
#ask us how tall we are then creates the variable height, that equals what we type in
print "how tall are you?",
height = raw_input()
#ask us how heavy we are then creates the variable weight, that equals what we type in
print "How much do you weigh?",
weight = raw_input()
#prints our age height and weight by using the modulus string thing
print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

print "Halt!"
s = raw_input("Who goes there? ")
print "You may pass,", s

name = raw_input('Enter your name : ')
print ("Hi %s, Let us be friends!" % name);


#more internet examples
print (30 * '-')
print ("  M A I N - M E N U")
print (30 * '-')
print ("1. Backup")
print ("2. User management")
print ("3. Reboot the server")
print (30 * '-')

## get input ##
choice = raw_input('Enter your choice [1-3] : ')

### convert string to int type ###
choice = int(choice)

#take action as per selection chosen#
if choice == 1:
    print ("Starting backup...")
elif choice == 2:
    print ("Starting user management...")
elif choice == 3:
    print ("Rebooting the server...")
else:
    print ("Invalid number. Try again...")
