# Here's another chance to practice your for loop skills. Write code for the
# function word_in_pos (meaning word in parts_of_speech), which takes in a string
# word and a list parts_of_speech as inputs. If there is a word in parts_of_speech
# that is a substring of the variable word, then return that word in parts_of_speech,
# else return None.
test_cases = ["NOUN", "PLURALNOUN", "NOUN", "FALSE", "<<@PERSON><", "PLURALNOUN"]
parts_of_speech = ["PERSON","PLURALNOUN", "NOUN","PLURALNOUN"]

def searchWordWithInPOS(POS, word):
    #print word, POS
    wLen = len(word)
    posLen = len(POS)
    count =0
    # print posLen - wLen +1
    while count < posLen - wLen +1:
        if POS[count: wLen +count] == word:
            # print POS[count: wLen +count]
            lst = POS[0:count], POS[count: wLen +count], POS[wLen +count:]
            print lst
            return True
        count = count +1
    return False


def word_in_pos(word, parts_of_speech):
    # your code here
    index = 0

    while index < len(parts_of_speech) :
        # print word, parts_of_speech[index]
        # print "index ", str(index) , " " , parts_of_speech[index]," ",word
        # print  "inside While"
        if parts_of_speech[index] == word:
            # print "Found"
            return word
        if searchWordWithInPOS(word, parts_of_speech[index]):
                return parts_of_speech[index]
                # print "test"

        index = index + 1


    return


# print test_cases[0], " ",word_in_pos(test_cases[0], parts_of_speech)
# print test_cases[1], " " , word_in_pos(test_cases[1], parts_of_speech)
# print test_cases[2], " " , word_in_pos(test_cases[2], parts_of_speech)
# print test_cases[3],  " " , word_in_pos(test_cases[3], parts_of_speech)
print test_cases[4],  " " , word_in_pos(test_cases[4], parts_of_speech)
print test_cases[5],  " " , word_in_pos(test_cases[5], parts_of_speech)
