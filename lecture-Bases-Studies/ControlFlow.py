def is_friend(name):
    check = name[0:1].upper()
    if check == 'D' or check == 'N':
        return True
    else:
        return False

print is_friend('Diane')
print is_friend('Nandy')
print is_friend('diane')
print is_friend('nandy')
print is_friend('11')
print is_friend('__')
print is_friend('')
print is_friend('dred')
print '--------------'

def biggest(one ,two ,thr):
    if one > two and one > thr:
        return one
    else:
        if two > thr:
            return two
    return thr



print biggest(3, 6, 9)
print biggest(6, 9, 3)
print biggest(9, 3, 6)
print biggest(3, 3, 9)
print biggest(9, 3, 9)
print biggest(-1,3,3)
print biggest(0,0,0)
