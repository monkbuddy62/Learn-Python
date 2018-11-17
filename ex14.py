# importing in the argv module! this is in sys so we need it from that
from sys import argv
# dunno why we need script here, but these 3 variables get created from the script name and the 2 things i type after that

script, user_name, penis = argv
# this is setting the variable prompt as the string '# '
prompt = '# '
#printing with variables init
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions. "
print " Do you like me %s?" % user_name
#THIS is setting up a variable, but making its contents what raw_input is grabbing from the user, while this is happening the variable, prompt, is being show to the user

#which happens to be #
likes = raw_input(prompt)

print "Where do you live %s" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

#millions of penis's
#three
#million penises... to be exact
print penis * (3000000)
