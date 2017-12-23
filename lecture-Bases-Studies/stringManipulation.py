# String Manipulation
# Write Python code that prints out the number of hours in 7 weeks.
week =7
days = 7
hr_in_day=24
hr_in_7_week = week*days*hr_in_day
print hr_in_7_week
#
s=''
str1 = ('a'+ s ) [1:]

str3 = s+ ''
str4 = s[0:]
print str1

print str3
print str4

s = 'udacity'
t = 'bodacious'
print s[0:2] + t[3:]

sentence = "A NOUN went on a walk. It can VERB really fast."
print sentence.find('VERB')
print  sentence[:2]

print sentence[6:30]
print sentence[34:]

text = "We believe university-level zip education can be both high quality and low cost. Using the economics of the Internet, we've connected some of the greatest teachers to hundreds of thousands of students all over the world."
pos1= text.find("zip") +3
print text[pos1:]
pos2 = text[pos1:].find("zip")
print pos2+3
print text[pos2:]
