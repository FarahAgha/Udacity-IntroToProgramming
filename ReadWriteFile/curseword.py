import urllib
def read_content():
    filename = "readCurseWordFile.txt"
    # path = "/Users/hellotofarah/Documents/Udacity-IntroToProgramming/ReadWriteFile"
    to_read = open (filename)
    content_read = to_read.read()
    result = check_profanity(content_read)
    to_read.close()

def check_profanity(text_to_chk):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_chk)
    result = connection.read()
    if 'true' in result:
        print ("Alert ")
    elif 'false' in result:
        print ("Now an Alert ")
    else:
        print ("Could not scan")
    connection.close()

read_content()
