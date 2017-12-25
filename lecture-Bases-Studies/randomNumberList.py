# from random import randint
import random as rand

def random_verb():
    random_num = rand.randint(0, 1)
    print random_num
    if random_num == 0:
        print "Lama"
        return "run"
    else:
        print "Lama"
        return "kayak"

def random_noun():
    random_num = rand.randint(0,1)
    print random_num
    if random_num == 0:
        print "sofa"
        return "sofa"
    else:
        print "Lama"
        return "llama"

def word_transformer(word):
    # your code here
    if word == "NOUN":
        print "Lama"
        return random_noun()
    if word == "VERB":
        print "Lama"
        return random_verb()

word  = "The sentence contains NOUN and a VERB see if it works"
# word = " NOUN is a name of person place or thing. what is VERB"
# word = "In english sometimes sentence ends with VERB"
print  word_transformer(word)
