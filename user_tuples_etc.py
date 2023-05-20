"""
Tuples and More (Task 5 from Project 3)

This is a script to practice with tuples, sets and dictionaries in the domain of food: Sarah's Sammie Shoppe

Author: Sarah DeConink

Task 5.1: Create some tuples and practice

Task 5.2: Create two sets and get the intersection and union of the sets

Task 5.3: Create a dictionary with key-value pairs of each word and its count from a file

"""

# import logging function
from util_datafun_logger import setup_logger
logger,logname = setup_logger(__file__)


# Task 5.1: Create some tuples and practice


# Create some tuples for the tables customers sat at in Sarah's Sammie Shoppe on different days
tupleMonday = (4, 8, 9, 10)
tupleTuesday = (9, 7, 8, 6)
logger.info("Task 5 - Tuples")
logger.info(f"The table #s used on Monday: {tupleMonday}")
logger.info(f"The table #s used on Tuesday: {tupleTuesday}")

# tuple concatenation - to find the tables that were used on Monday and Tuesday
tupleTable = tupleMonday + tupleTuesday
logger.info(f"The table #s used on Monday and Tuesday: {tupleTable}")

# tuple repetition
tupleTwice = tupleTable * 2
logger.info(f"The table #s used on might be used on by the time we get to Thursday: {tupleTwice}")

# tuple membership testing

hasOne = 1 in tupleTable
logger.info(f"Was Table 1 used on Monday or Tuesday: {hasOne}")
hasSix = 6 in tupleTable  # False
logger.info(f"Was Table 6 used on Monday or Tuesday: {hasSix}")

# tuple indexing (0 is first, -1 is last, or 1 less than the length)

logger.info(f"What was the 3rd table to be used on Monday? Table #{tupleMonday[2]}")
logger.info(f"What was the last table to be used on Tuesday? Table #{tupleTuesday[-1]}")
logger.info("")


# Task 5.2: Create two sets and get the intersection and union of the sets
logger.info("Task 5 - Sets")

SetUniversal = {'BLT', 'Fried Chicken', 'Flank Steak', 'Sliced Turkey', 'Pulled Pork', 'Portabella Mushroom'}
logger.info(f"Here are all the sandwich choices: {SetUniversal}")

SetMondayOrders = {'Flank Steak', 'Fried Chicken', 'Portabella Mushroom'}
logger.info(f"Here are the sandwiches ordered on Monday: {SetMondayOrders}")

SetTuesdayOrders = {'Fried Chicken', 'Pulled Pork', 'Portabella Mushroom'}
logger.info(f"Here are the sandwiches that were ordered on Tuesday: {SetTuesdayOrders}")

SetUnion = SetMondayOrders | SetTuesdayOrders
logger.info(f"Here are all of the menu items that were ordered on Monday and Tuesday: {SetUnion}")

SetIntersection = SetMondayOrders & SetTuesdayOrders
logger.info(f"Here were the menue items that were ordered on both Monday and Tuesday: {SetIntersection}")

SetDifference = SetUniversal - SetUnion
logger.info(f"Here were the menue items that were not ordered on Monday and Tuesday: {SetDifference}")
logger.info("")


# Task 5.3: Create a dictionary with key-value pairs of each word and its count from a file
logger.info("Task 5 - Dictionaries")
with open("text_names_in.txt") as file_object:
    word_list = file_object.read().split()

word_counts_dict = {}
word_counts_dict = {word: word_list.count(word) for word in word_list}
logger.info(f"Here is the key-value pairs of words : word count in the text_names_in.txt file: {word_counts_dict}")


