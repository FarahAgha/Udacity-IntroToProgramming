import random

# IPND Stage 2 Final Project
# Done TO DO add more items in each list
# if user select 1
list_easy = [['''__5__ twinkle __1__ star.
how I __2__? What you are?
Up above the __3__ so high
like a __4__ in the sky. ''',
["little", "wonder", "world", "diamond","Twinkle"]],
['''__1__ and __2__
Went up the __3__
To fetch a __4__ of water
__1__ fell down
And broke his __5__ ,
And __2__ came tumbling after''',
["Jack", "Jill", "hill", "pail", "crown"]]]

# if user select 2
list_mod =[
['''Five little __1__ jumping on the bed
One __3__ off and bumped his __4__
Mama called the __2__
And the __2__ said
No more __1__ jumping on the bed''' ,
["monkeys", "doctor", "fell", "head"]],
[''' Bear In There ~ by Shel Silverstein
There's a __1__ Bear
In our __4__
__3__ likes it 'cause it's cold in there.
With his seat in the meat
And his face in the fish
And his big hairy paws
In the buttery dish,
__2__ nibbling the noodles,
__2__ munching the rice,
__2__ slurping the soda,
__2__ licking the ice.
And __3__ lets out a roar
If you open the door.
And it gives me a scare
To know __2__ in there--
That Polary Bear
In our __4__.''',
["Polar", "He's", "he","Fridgitydaire" ]]]
# if user select 3
list_diff = [['''Freedom __1__ standing on a mountain
In a foreign __2__
Trying to send a __3__
To his people, back in the __4__
He had a __5__ one time''',
["fighter", "country", "message", "ghetto", "home"]],
['''People are often unreasonable, irrational, and self-centered.  Forgive them __1__.
If you are kind, people may accuse you of selfish, ulterior motives.  Be kind __1__.
If you are __2__, you __will win some unfaithful friends and some genuine enemies.  Succeed __1__.
If you are honest and sincere people may deceive you.  Be honest and sincere __1__.
What you spend years creating, others could destroy overnight.  Create __1__.
If you find serenity and happiness, some__ may be jealous.  Be happy __1__.
The good you do __3__, will __often be forgotten.  Do good __1__.
Give the best you have, and it will never be enough.  Give your best __1__.
In the final analysis, it is between you and God.  It was never between you and them __1__. ''',
["anyway","successful","today"]]]
# Check if place of the blank number and replace it with the word in the list
# find the number for a  blank space

# to extract number from the numbered blank space e.g. 12 from __12__
def extract_blank_number(word):
    num = 0
    index = 0
    while index <len(word):
        p = word[index]
        if p != '_':
            num = num * 10 + int(p)
        index = index + 1
    return num
"""Returns blanks filled string by taking string to be replaced and answer list along with number of blanks user filled. """
def replace_blank_index_with_word(list_choosen_string,list_choosen_answers, blank_number):
    # list_choosen_string = list_choosen[0]
    # list_choosen_answers = list_choosen[1]
    to_fill_string = list_choosen_string.split()
    filled_string =""

    for word in to_fill_string:
        if "__"  in word:
            loc1 - word.find("__")
        if word[0] =='_':
            if word[-1] == '_':
                num = extract_blank_number(word)
                if num == blank_number+1:
                    word = list_choosen_answers[num-1]
            # in case user ans added punctuation
            elif word[-2] == '_':
                punc = word[-1]
                num = extract_blank_number(word[0:len(word)-1])
                if num == blank_number+1:
                    word = list_choosen_answers[num-1]+punc

        filled_string = filled_string + " " + word
    return"".join(filled_string)
list_choosen_string = "test__1__test"
list_choosen_answers= ["anyway","successful","today"]
blank_number = 1
print replace_blank_index_with_word(list_choosen_string,list_choosen_answers, blank_number)

def replace_blank_index(list_choosen,index):
    # list_choosen_string = list_choosen[0]
    list_choosen_answers = list_choosen[1]
    count =0
    filled_list = list_choosen[0] #list_choosen_string
    while count < index:
        filled_list = replace_blank_index_with_word(filled_list,list_choosen_answers, count)
        count =count +1
    return filled_list

def player_guesses(list_choosen):
    # list_choosen_string = list_choosen[0]
    list_choosen_answers = list_choosen[1]
    index = 0

    filled_list =list_choosen[0]
    print filled_list
    print
    for word in list_choosen_answers:
        attempt = 0
        while attempt <5:
            str_with_number = "Enter your choice for __"+str(index+1)+"__  "
            user_input = (raw_input( str_with_number))
            if user_input.upper() == list_choosen_answers[index].upper():
                filled_list = replace_blank_index(list_choosen,index+1)
                print
                print filled_list
                break
            else:
                print attempt+1 ," out of 5 wrong attempts"
                attempt = attempt+1
        if attempt == 5:
            print "You've failed too many straight guesses!  Game over!"
            break
        index = index + 1

def random_list_location():
    # Done TO DO if user select 1, 2 or 3  use Randon function to select the quize from the list
    rand_int =  random.randint(0,1)
    return rand_int

def game_instructions():
    print
    print "Choose difficulty level"
    print "1. Easy"
    print "2. Moderate"
    print "3. Difficult"
    print

def launch_game(list_choosen):
    num = random_list_location()
    random_list_for_user = list_choosen[num]
    player_guesses(random_list_for_user)

def fill_blank_game():
    print
    print "Welcome to the Fill in the Blank Game"
    choice = 'y'
    # Done TO DO The continue message should show the valid reponses for continuing(Y or y) and not continuiing(e.g. N or n)
    while choice =='Y' or choice =='y':
        game_instructions()
        # done TO DO ask user for the dificulty level
        user_input = (raw_input("Enter your choice now : " ))
        if user_input == '1':
            launch_game(list_easy)
        elif user_input == '2':
            launch_game(list_mod)
        elif user_input == '3':
            launch_game(list_diff)
        else :
            # DoneTODO Any number other then required numbers should show a message with the valid inputs
            print
            print "Incorrect choice ......."
        print
        choice =  raw_input( "Press Y or y if you still want to play. Any other key to quit ... ")

# fill_blank_game()
