tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
# does this make a noise?
# print "te\ast"
print "\"testes\""
print "te\bst" # print a backspace, dunno when id use it
print "te\fst" #new line tiny indent
print "te\nst"#new line
print "te\rst"
print "car\rriage return"

print "te\1st\1\1\1\1\1\1\n\2\2\2\2\2\n\3\3\3\3\3"
print "\4\5\6\7\0"
print "test\vtest"
#while True:
 #   for i in ["\2","\3","\4","\5","\6"]:
  #      print "%s\r" % i,
        
print '''
test
test 
big ol pair of testes
test
blah blah bliddity blah blah blah
'''

print u"\u041b"

print "test test test %s test test test" % 'TEST'
print "\ntest test test %r test test" % """test"""
