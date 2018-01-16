import random

# IPND Stage 2 Final Project
# Done TO DO add more items in each list
# if user select 1
list_easy = [['''Twinkle twinkle __1__ star.
how I __2__? __What__ you are?
Up above__ the __3__ so __high
like a __4__ in the sky. ''',
["little", "wonder", "world", "diamond"]],
['''__1__ and __2__
__Went__ up the __3__
To __fetch a __4__ of water
__1__ fell down__
And broke his crown ,
And __2__ came tumbling after''',
["Jack", "Jill", "hill", "pail"]]]

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
And it gives me a __4__
To know __2__ in there--
That Polary Bear
In our __5__.''',
["Polar", "He's", "he","scare","Fridgitydaire" ]]]
# if user select 3
list_diff = [['''Freedom __1__ standing on a mountain
In a foreign __2__
Trying to send a __3__
To his people, back in the __4__
He had a __5__ one time''',

["fighter", "country", "message", "ghetto", "home"]],
['''People are often unreasonable, irrational, and self-centered.  Forgive them __1__.
If you are kind, people may accuse you of __2__, ulterior motives.  Be kind __1__.
If you are __3__, you __will win some __4__ friends and some genuine enemies.  Succeed __1__.
If you are honest and sincere people may deceive you.  Be honest and sincere __1__.
What you spend years creating, others could destroy overnight.  Create __1__.
If you find serenity and happiness, some__ may be jealous.  Be happy __1__.
The good you do __5__, will __often be forgotten.  Do good __1__.
Give the best you have, and it will never be enough.  Give your best __1__.
In the final analysis, it is between you and __6__.  It was never between you and them __1__. ''',

["anyway","selfish", "successful", "unfaithful" ,"today","God"]]]

# Check if place of the blank number and replace it with the word in the list
# find the number for a  blank space
def replace_blank_index_with_word(list_choosen_string,list_choosen_answers, blank_number):
    """Short summary: to extract number out of a string and replace it in the string (only one blank at a time)

    Parameters
    ----------
    list_choosen_string : String
        A string based on difficulty level selected by the user
    list_choosen_answers : List
        A list of answers based on user choice of difficulty level
    blank_number : Integer
        Count of blanks spaces to be filled

    Returns
    -------
    List
        A list Filled with blank spaces

    """
    to_fill_string = list_choosen_string.split()
    filled_string = ""
    for word in to_fill_string:
        if "__"  in word:
            subword = ""
            loc1 = word.find("__") #4
            loc2 = word.find("__",loc1+2) #9
            if loc2 != -1:
                extracted = word[loc1+2:loc2]
                # check if the extracted word is digit
                if extracted.isdigit() and  int(extracted) == blank_number+1:
                    word = word[0:loc1]+list_choosen_answers[blank_number]+word[loc2+2:]
        filled_string = filled_string + " "+word
    # return as a list as its called in the same manner again
    return "".join(filled_string)


def replace_blank_index(list_choosen,index):
    """Short summary: replaces the blanks till given index values based on the list chosen by the user
    loop over number of values user input and replace with helper function  by govong the list
    with fill in the blank string and list of its answer along with number of values user has entered

    Parameters
    ----------
    list_choosen : List
        a list based on difficulty level selected by the user.
    index : Integer
        Count of blanks spaces to be filled

    Returns
    -------
    List
        A list Filled with blank spaces

    """
    # list_choosen_string = list_choosen[0]
    list_choosen_answers = list_choosen[1]
    count =0
    filled_list = list_choosen[0] #list_choosen_string
    while count < index:
        #func(filled_list,list_choosen_answers, count)
        filled_list = replace_blank_index_with_word(filled_list,list_choosen_answers, count)
        count =count +1
    return filled_list

# player entered blank value is checked user have 5 attemps to guess the blank
def player_guesses(list_choosen):
    """
    Short summary: Ask the player to guess a blank, When player guesses correctly,
    shows with correct answer with filled blank in the previous blank
    and shows a new prompt for the next blank

    Parameters
    ----------
    list_choosen : List
        the parameter `list_choosen` is the difficulty level seleceted by the user

    Returns
    -------
    None

    """
    # list_choosen_string = list_choosen[0]
    list_choosen_answers = list_choosen[1]
    index = 0

    filled_list =list_choosen[0]
    print filled_list
    print
    for word in list_choosen_answers:
        attempt ,max_try = 0, 5
        max_try=5
        while attempt <max_try:
            str_with_number = "Enter your choice for __"+str(index+1)+"__  "
            user_input = (raw_input( str_with_number))
            if user_input.upper() == list_choosen_answers[index].upper():
                # When player guesses correctly,
                # new prompt shows with correct answer in the previous blank
                # and a new prompt for the next blank
                filled_list = replace_blank_index(list_choosen,index+1)
                print
                print filled_list
                break
            else:
                # When player guesses incorrectly, they are prompted to try again
                print attempt+1 ," out of 5 wrong attempts"
                attempt = attempt+1
        if attempt == max_try:
            # Let the user decide how many wrong guesses they can make before they lose
            print "You've failed too many straight guesses!  Game over!"
            break
        index = index + 1

# quiz in the oth location or 1st location to be presented randomly to the user
def random_list_location():
    """Short summary: returns a randon number between 0 & 1

    Parameters
    ----------
    None

    Returns
    -------
    Integer
        randomly generated number

    """
    # Done TO DO if user select 1, 2 or 3  use Randon function to select the quize from the list
    rand_int =  random.randint(0,1)
    return rand_int

# Guide- How to of the game
def game_instructions():
    """Short summary: Shows the games instructions to the user

    Parameters
    ----------
    None

    Returns
    -------
    None

    """
    print
    print "Choose difficulty level"
    print "1. Easy"
    print "2. Moderate"
    print "3. Difficult"
    print

#when game launched, selection of the list presented randomly to the user, and given an opportunity to guess
def launch_game(list_choosen):
    """Short summary: Based on the difficulty level selected by the user. It randomly selects the quiz
    from the list. Then asks the user to guess.

    Parameters
    ----------
    list_choosen : List
        a list based on difficulty level selected by the user.

    Returns
    -------
    None

    """
    num = random_list_location()
    random_list_for_user = list_choosen[num]
    # Once a level is selected, game displays a fill-in-the-blank and a prompt to fill in the first blank.
    player_guesses(random_list_for_user)

# Main of the game. The program will start by invoking the function fill_blank_game
def fill_blank_game():
    """Short summary: The game has 3 levels and each level contains 4 or more blanks to fill in
    it ask user after playing game, if they wanted to play another time

    Parameters
    ----------
    None

    Returns
    -------
    None

    """
    print
    print "Welcome to the Fill in the Blank Game"
    choice = 'y'
    # Done TO DO The continue message should show the valid reponses for continuing(Y or y) and not continuiing(e.g. N or n)
    while choice =='Y' or choice =='y':
        game_instructions()
        # done TO DO ask user for the dificulty level
        # Immediately after running the program, user is prompted to select a difficulty level from easy / medium / hard
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

# the games started by invoking the fill_blank_game() function
fill_blank_game()
