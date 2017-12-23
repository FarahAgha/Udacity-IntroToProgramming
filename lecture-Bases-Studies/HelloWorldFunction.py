#Function hello World

def hello():
  return "Hello world"+"!"*3

print hello

def textNum(var1, var2):
    print var1 , var2*2
    print id(var1)
    print id(var2)

textNum("hello Farah",555)

def square(number):
    return number * number

print square(9)
print square(0)
print square(-15)
print square(square(-5))

def sum3(var1, var2, var3):
    return var1+ var2 + var3

print sum3(1,2,3)
print sum3(1,2,-3)
print sum3(1,0,3)
print sum3(0,0,0)
print sum3(-1,-1,-1)

def abbaize(val1, val2):
    return val1+val2*2+val1

print abbaize('a','b')
print abbaize('dog','cat')

def udacify(val1):
    return 'u'+val1

print udacify('farah')
