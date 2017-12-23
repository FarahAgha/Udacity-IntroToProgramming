stooges = ['Moe', 'Larry', 'Curly']
print stooges

spy = [0,0,7]
agent = spy
print agent[2]
spy[2] = agent[2] + 1
print agent[2]


def replace_spy(spy):
    spy[2] = spy[2]+1

spy = [0,0,7]

replace_spy(spy)
print spy

stooges.append("Shemp")
print stooges

p = [1,2]
p.append(3)
p = p + [[1,'a']]
print p
print len(p)

for e in p:
    print e

def sum_list(p):
    sum =0
    for e in p:
        sum = sum + e
    return sum

print sum_list([1, 7, 4])
#>>> 12

print sum_list([9, 4, 10])
#>>> 23

print sum_list([44, 14, 76,1,-44])
#>>> 134

def measure_udacity(p):
    count =0
    for e in p:
        if e[0] == 'U':
            count = count + 1
    return count

print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0
print measure_udacity(['Umika','Umberto'])
#>>> 2

def find_element(lis, val):
    found = -1
    count =0
    for e in lis:
        if e == val:
            found = count
            break;
        count = count +1
    return found
print find_element([1,2,3],1)
print find_element(['CS101', 'CS373', 'CS212', 'CS101', 'CS373', 'CS262'], 'CS101')
