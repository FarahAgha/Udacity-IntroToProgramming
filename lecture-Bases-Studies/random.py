# from random import randint
import random as rand

def random_verb():
    random_num = rand.randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"

def random_noun():
    random_num = rand.randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def word_transformer(word):
    # your code here
    if word == "NOUN":
        return random_noun()
    if word == "VERB":
        return random_verb()

word  = "The sentence contains NOUN and a VERB see if it works"
# word = " NOUN is a name of person place or thing. what is VERB"
# word = "In english sometimes sentence ends with VERB"
print  word_transformer(word)
