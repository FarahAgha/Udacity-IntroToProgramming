# IPND Stage 2 Final Project
#
import random
# Global Variable
# to hold List item
list_choosen = ["",[]]
# to hold fill in the blank string
list_choosen_string = list_choosen[0]
# to hold list of answers
list_choosen_answers = list_choosen[1]
# to hold number of tries for incorrect answers
max_try =5


# Done TO DO add more items in each list
1# if user select 1
list_easy = [['''Twinkle twinkle__1__star.
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


# Fill the string with answer for blank space
def replace_blank_index_with_word(filled_list,blank_number):
    """Short summary: to extract number out of a string and replace it in the string (only one blank at a time)

    Parameters
    ----------
    filled_list : String
        A string based on difficulty level selected by the user
    blank_number : Integer
        Count/number of the blanks spaces to be filled

    Returns
    -------
    String
        A string Filled with blank spaces

    """
    replace_blank = "__"+str(blank_number+1)+"__"

    filled_list = filled_list.replace(replace_blank, list_choosen_answers[blank_number])

    return filled_list

def replace_blank_index(index):
    """Short summary: replaces the blanks till given index values based on the list chosen by the user
    loop over number of values user input and replace with helper function  by govong the list
    with fill in the blank string and list of its answer along with number of values user has entered

    Parameters
    ----------
    index : Integer
        Count of blanks spaces to be filled

    Returns
    -------
    String
        A string Filled with blank spaces

    """

    count =0
    filled_list = list_choosen_string
    # looping over each word in the string to replace blank
    while count < index:
        filled_list = replace_blank_index_with_word(filled_list,count)
        count =count +1

    return filled_list

# player entered blank value is checked user have 5 attemps (set as global) to guess the blank
def player_guesses():
    """
    Short summary: Ask the player to guess a blank, When player guesses correctly,
    shows with correct answer with filled blank in the previous blank
    and shows a new prompt for the next blank

    Parameters
    ----------
    None

    Returns
    -------
    void

    """
    #Done TO DO reduce size to 18 lines
    index = 0
    print list_choosen_string

    for word in list_choosen_answers:
        attempt  = 0

        while attempt < max_try:
            str_with_number = "\nEnter your choice for __"+str(index+1)+"__  \n"
            user_input = (raw_input( str_with_number))
            # When player guesses correctly,
            if user_input.upper() == list_choosen_answers[index].upper():
                # and a new prompt for the next blank
                filled_list = replace_blank_index(index+1)
                # new prompt shows with correct answer in the previous blank
                print filled_list
                break
            else:
                # When player guesses incorrectly, they are prompted to try again
                print "\n",attempt+1 ," out of ",max_try ," wrong attempts"
                attempt = attempt+1
        if attempt == max_try:
            # Let the user decide how many wrong guesses they can make before they lose
            print "\nYou've failed too many straight guesses!  Game over!"
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
    void

    """
    print "\nChoose difficulty level"
    print "1. Easy"
    print "2. Moderate"
    print "3. Difficult\n"


#when game launched, selection of the list presented randomly to the user, and given an opportunity to guess
def launch_game(list_choosen_by_user):
    """Short summary: Based on the difficulty level selected by the user. It randomly selects the quiz
    from the list. Then asks the user to guess.

    Parameters
    ----------
    list_choosen_by_user : List
        a list based on difficulty level selected by the user.

    Returns
    -------
    void

    """
    # set the values to be used globally
    global list_choosen, list_choosen_string, list_choosen_answers
    num = random_list_location()
    list_choosen =list_choosen_by_user[num]
    list_choosen_string = list_choosen[0]
    list_choosen_answers =list_choosen[1]

    # Once a level is selected, game displays a fill-in-the-blank and a prompt to fill in the first blank.
    player_guesses()

# Main of the game. The program will start by invoking the function fill_blank_game
def fill_blank_game():
    """Short summary: The game has 3 levels and each level contains 4 or more blanks to fill in
    it ask user after playing game, if they wanted to play another time

    Parameters
    ----------
    None

    Returns
    -------
    void

    """
    print "\nWelcome to the Fill in the Blank Game"
    choice = 'y'
    # Done TO DO The continue message should show the valid reponses for continuing(Y or y) and not continuiing(e.g. N or n)
    while choice.upper() =='Y':
        game_instructions()
        # done TO DO ask user for the dificulty level
        # Immediately after running the program, user is prompted to select a difficulty level from easy / medium / hard
        user_input = (raw_input("\nEnter your choice now : " ))
        if user_input == '1':
            launch_game(list_easy)
        elif user_input == '2':
            launch_game(list_mod)
        elif user_input == '3':
            launch_game(list_diff)
        else :
            # DoneTO DO Any number other then required numbers should show a message with the valid inputs
            print "\nIncorrect choice ......."
        choice =  raw_input( "\nPress Y or y if you still want to play. Any other key to quit ... ")

# the games started by invoking the fill_blank_game() function
fill_blank_game()
