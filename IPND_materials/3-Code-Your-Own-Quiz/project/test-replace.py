#dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# print "dict['Name']: ", dict['Name']
# print "dict['Age']: ", dict['Age']
#

fill_in_quiz = {
"list_easy" :['''__1__ twinkle __2__ star''',["Twinkle", "little"]],
"list_mod"  :['''Five little __1__ jumping on the __2__''',["monkeys","bed"]],
"list_diff" :['''Freedom __1__ __2__ on a __3__''',["fighter","standing","mountain"]]}
print "fill_in_quiz['Name']: ", fill_in_quiz['list_easy']

a = fill_in_quiz['list_easy']
print a[0] , " ___ ",a[1]

print fill_in_quiz['list_easy'][0]
