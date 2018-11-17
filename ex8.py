
# creates the variable as a string, but a string of conditional formatty things
formatter = "%r %r %r %r"

# prints the contents of the variable then putting in 1 2 3 and 4
print formatter % (1, 2, 3, 4)
# prints the contents of the variable but one two three four gets injected in
print formatter % ("one", "two", "three", "four")
# same as above but prints the True's and Falses
print formatter % (True, False, False, True)
# prints the contents of formatter 4 times
print formatter % (formatter, formatter, formatter, formatter)
# prints the strings that follow, the commas make them appear on the same line I think.
print formatter % (
    "I had this thing.", # why do I need these commas?
    "That you could type up right.",
    "But it didn't sing.",
    "So I said gooodnight."
    )
