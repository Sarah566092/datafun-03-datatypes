"""
Optional bonus. See course site for details.

>>> len(longwordset1)
415

>>> len(longwordset2)
197

>>> len(longwords)
13
"""

import doctest

from util_datafun_logger import setup_logger
logger,logname = setup_logger(__file__)


# read from second file and get a list of words

with open("text_hamlet.txt", "r") as f1:
    text = f1.read()
    wordlist1 = text.split()  # split on whitespace

# read from second file and get a list of words

with open("text_juliuscaesar.txt", "r") as f2:
    text = f2.read()
    wordlist2 = text.split()  # split on whitespace

# Done with files - let the files close and the work begin

# Remove duplicates by creating two sorted sets
# hint: use sorted() to sort the list
# hint: use set() to remove duplicates
# name them wordset1 and wordset2
wordset1 = set(sorted(wordlist1))  # TODO fix this line
wordset2 = set(sorted(wordlist2))  # TODO fix this line


# initialize a variable maxlen = 10
maxlen = 10  # TODO fix this line

# use a list comprension to get a list of words longer than 10

# for word in wordset1
# That is:
# in a list (e.g. square brackets)
# say "[Give me word (for each word in wordset1)
#      if len(word) is greater than maxlen]"
# then convert the list to a set to we can take the intersection
# hint: use set()
# name them longwordset1 and longwordset2

longwordset1 = set([word for word in wordset1 if len(word) > maxlen])
longwordset2 = set([word for word in wordset2 if len(word) > maxlen])

# find the intersection of the two sets
# that is, the words in both longwordset1 1 & longwordset2
# name this variable longwords
longwords = longwordset1 & longwordset2

# print the length of the sets and the list
logger.info(f"There are {len(longwordset1)} unique words in Hamlet that are longer that {maxlen} letters")
logger.info(f"There are {len(longwordset2)} unique words in Julius Ceasar that are longer that {maxlen} letters")
logger.info(f"There are {len(longwords)} that are in both of the plays.")
logger.info("")
logger.info(f"Here are these {sorted(longwords) = }")
logger.info("")

# check your work
logger.info("TESTING...if nothing prints before the testing is done, you passed!")
doctest.testmod()
logger.info("TESTING DONE")

def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())