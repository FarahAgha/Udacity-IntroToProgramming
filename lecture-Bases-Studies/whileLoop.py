def remove_space(text):
    new_text=""

    while text !='':
        if text[0] != ' ':
            new_text = new_text + text[0]
        text = text[1:]

    return new_text

print "name" + remove_space("farah agha")
print remove_space(" farah agha ") + "name"

def print_numbers(num):
    count = 0
    while count < num:
        count = count + 1
        print count

print print_numbers(-1)

def print_numbers_break(num):
    count = 0
    while True:
        if count < num:
            count = count + 1
            print count
        else:
            break

print print_numbers_break(10)
