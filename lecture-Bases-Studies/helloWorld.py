print 'hello World!!'

speed_of_light = 299792458.0
cycles_per_second = 2700000000.0

name = "arah's"
print " Name %s" , name
print 'C:\\nowhere' + name +'welcome'

s="MonoChrome"
print s[3], s[1+1+1]
print s[0], (s + s)[0]
print s[0] + s[1], s[0 + 1]
print s[1] , (s + 'ity')[1]
print s[-1], (s + s)[-1]
print (s + 'ity')[1], s[1]
print s.capitalize()
print s[1:].capitalize()
print s+s[0:-1+1]
print s[:3]+s[3:]
print s[:-1]

s="any string"
print s.find(s)
print s.find('s')
print 's'.find('s')
print s.find('')

print "Example 1: using find to print the second occurrence of a sub-string"
print "test".find("t")
print "test".find("t", 1)

print "Example 2: using a variable to store first location"
first_location = "test".find("t") # here we store the first location of "t"
print "test".find("t", first_location+1) # then we use that location to find the second occurrence.

print "Example 3: using find to get rid of exclamation marks!!"
example = "Wow! Python is great! Don't you think?"
first = example.find('!')
second = example.find('!', first + 1)
new_string = example[:first] + example[first+1:second] + example[second+1:]
print new_string # oops, I should probably replace the !s with periods
new_string = example[:first] +'.'+ example[first+1:second] +'.'+ example[second+1:]
print new_string
