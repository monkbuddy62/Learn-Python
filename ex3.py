import decimal

# This starts off the example saying were gonna count some chickennsss
print "I will now count my chickens:"

# This follows PEMDAS and divides 30 by 6 getting 5 then adds that to 25
print "Hens", 25.0 + 30.0 / 6.0
# Here  we count roosters, first 25 * 3 is 75, 4 goes into 75 18 times with remainder 3
# so 3 is our modulo number, 100 - 3 is 97
print "Roosters", 100.0 - 25.0 * 3.0 % 4.0

print "Now I will count the eggs:"

#do the multiplicating and dividing and modulo first, starting from left to right
#4 % 2 is 0 becuase 2 goes into 4 2 times with NO remainder, move on to the division 1/4 is 0 when we dont have floating point decimals. so 3+2+1-5+0-0+6=7
print 3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0

print "Is it true that 3.0 + 2.0 < 5.0 - 7.0?"
#we are stating that 5 is less than -2 which python reports is False
print 3.0 + 2.0 < 5.0 - 7.0
#printing and mathing
print "What is 3.0 + 2.0?", 3.0 + 2.0
#printing and mathing
print "What is 5.0 - 7.0?", 5.0 - 7.0

print "Oh, that's why it's False."

print "How about some more."
#printing and making a statement that we know python with report as True
print "Is it greater?", 5.0 > -2.0
#Since 5 is greater than or equal to 2 python prints out True
print "Is it greater or equal?", 5.0 >= -2.0
#simce 5 is not less than or equal to -2 python prints out False
print "Is it less or equal?", 5.0 <= -2.0
