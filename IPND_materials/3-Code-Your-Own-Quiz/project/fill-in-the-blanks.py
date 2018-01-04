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
If you are __2__, you will win some unfaithful friends and some genuine enemies.  Succeed __1__.
If you are honest and sincere people may deceive you.  Be honest and sincere __1__.
What you spend years creating, others could destroy overnight.  Create __1__.
If you find serenity and happiness, some may be jealous.  Be happy __1__.
The good you do __3__, will often be forgotten.  Do good __1__.
Give the best you have, and it will never be enough.  Give your best __1__.
In the final analysis, it is between you and God.  It was never between you and them __1__. ''',
["anyway","successful","today"]]]
# Check if place of the blank number and replace it with the word in the list
# find the number for a  blank space
def blank_number(place):
    num = 0
    index = 0
    while index <len(place):
        p = place[index]
        if p != '_':
            num = num * 10 + int(p)
        index = index + 1
    return num

def blank_word(blank_word, answer_List):
    num = blank_number(blank_word)
    assert num >0 and num <= len(answer_List),"invalid number in blank space, Check words in the list"
    return answer_List[num-1][1]

def replace_blank(list_quiz,answer_List):
    quiz_string = list_quiz[0].split()
    # search blank number position and replace
    answer_string = ''
    # search if the word has blank_number in it
    for word in quiz_string:
        # print blank_word
        if word[0] =='_':
            if word[-1] == '_':
                word = blank_word(word, answer_List)
            # Done TO Do handle punctuations
            elif word[-2] == '_':
                punc = word[-1]
                word = word[0:len(word)-1]
                word = blank_word(word, answer_List)
                word = word + punc
        answer_string = answer_string + " " + word
        # TO DO Concatenate string convert it back to list
        new_List = "".join(answer_string)
    print new_List

def random_list_location():
    # Done TO DO if user select 1, 2 or 3  use Randon function to select the quize from the list
    rand_int =  random.randint(0,1)
    return rand_int

def serve_String(list_ch):
    print list_ch[0]

def user_answer_list(list_ch):
    list_length =  len(list_ch[1])
    count =0
    user_list = []
    while count < list_length:
        str_with_number = "Enter your choice for "+str(count+1)+" : "
        # Done TO DO: User answer Input
        user_input = (raw_input( str_with_number))
        # if user_input != list_ch[rand_int][1][count]:
        item = [count , user_input]
        user_list.append(item)
        count  = count +1
    return user_list

def display_incorrect(list_ch, user_list):
    list_length =  len(user_list)
    count =0
    while count < list_length:
        # Done TO DO ignore Case for user inputs
        if user_list[count][1].upper() != list_ch[1][count].upper():
            print "Incorrect Value ", user_list[count][1], " at location ",user_list[count][0]+1
        count = count + 1

def game_instructions():
    print
    print "Choose difficulty level"
    print "1. Easy"
    print "2. Moderate"
    print "3. Difficult"
    print

def launch_game(list_ch):
    # done TO DO generate random list 0 or 1
    rand_int = random_list_location()
    # done TO DO based on generated number sever the sting with blank
    serve_String(list_ch[rand_int])
    # done TO DO ask user to input corrosponding values
    # and check user input with quiz answer list store it in list
    user_list = user_answer_list(list_ch[rand_int])
    # done TO DO display incorrect answeres if any/ congratulation message
    display_incorrect(list_ch[rand_int], user_list)
    replace_blank(list_ch[rand_int],user_list)

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
        if user_input == '2':
            launch_game(list_mod)
        if user_input == '3':
            launch_game(list_diff)
        else :
            # DoneTODO Any number other then required numbers should show a message with the valid inputs
            print
            print "Incorrect choice ......."
        print
        choice =  raw_input( "Press Y or y if you still want to play. Any other key to quit ... ")


fill_blank_game()
