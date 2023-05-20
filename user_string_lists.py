"""
This script will use String Lists to help design a creative menu for Sarah's Sammie Shoppe

Author: Sarah DeConink

List_1 will use Python's built-in functions to work with lists of words for the menu
List_2 will randomly create sandwich choices
List_3 will use a text data file in this repo to get a list of unique words

"""

# imports first
import random

# import logging function
from util_datafun_logger import setup_logger
logger,logname = setup_logger(__file__)


# Define shared data ..........................................


# Define a list of sandwich names
list_names = ["BLT", "Fried Chicken", "Flank Steak", "Sliced Turkey", "Pulled Pork", "Portabella Mushroom"]

# Define a list of intro adjectives
list_marketing_adjectives = ["Dynamic", "Subtle", "Juicy", "Stellar", "Fresh", "Jammin"]

# Define a list of veggie toppings
list_veggies = ["lettuce", "jalapenos", "grilled peppers", "onions", "tomato", "pickles"]

# Define a list of cheeses
list_cheeses = ["colby", "pepper jack", "american", "cheddar", "provolone", "Gruyere"]

# Define a list of spreads
list_spreads = ["mayonnaise", "garlic aioli", "honey mustard", "guacamole", "ranch", "pepper BBQ"]


# Give user info
def menu_info():
    
    logger.info("Let's create 5 lists of words that we could use in our menu for Sarah's Sammie Shoppe.")
    logger.info(f"The sandwich names: {list_names}")
    logger.info(f"The veggie toppings: {list_veggies}")
    logger.info(f"The cheeses: {list_cheeses}")
    logger.info(f"The spreads: {list_spreads}")
    logger.info(f"The marketing adjectives: {list_marketing_adjectives}")

# String Lists 1. Using Python built-in functions to understand information about our menu choices

def menu_built_in_funtctions():
    """Give data on menu choices"""
    
    logger.info("")
    logger.info("String Lists 1. Using Python Built-in Functions")
   
    # Create a tuple to manipulate choices if needed
    menu_tuple = list(zip(list_names, list_marketing_adjectives, list_veggies, list_cheeses, list_spreads))
    logger.info(f"Here are all of the words that we can choose from in a tuple if needed: {menu_tuple}")

    names_length = len(list_names)
    veggies_length = len(list_veggies)
    cheese_lengeth = len(list_cheeses)
    spread_length = len(list_spreads)
    
    logger.info(f"There are a {names_length} types of sandwiches, {veggies_length} types of veggies, {cheese_lengeth} types of cheeses, and {spread_length} types of spreads.")
    
    all_menu_words = list(list_names + list_veggies + list_cheeses + list_spreads)
    menu_words_length = len(all_menu_words)
    menu_words_set = len(set(all_menu_words))
    logger.info(f"There are a total of {menu_words_length} words used in the choices and a total of {menu_words_set} unique words")

    if menu_words_length == menu_words_set:
        logger.info(f"There are no repeated words in the menu choices.")
        logger.info("")
    else:
        logger.info(f"There are repeated words in the menu choices")
        logger.info("")


# String Lists 2. Random Choice

def create_random_sandwiches():
    """Create a random sentence from our pre-defined lists"""
    logger.info("String Lists 2. Calling create_random_sandwich()")
    
    # Create a random sandwiches
    sandwich = (
        f"The {random.choice(list_marketing_adjectives)} {random.choice(list_names)} "
        f"with {random.choice(list_veggies)}, {random.choice(list_cheeses)} cheese, and {random.choice(list_spreads)} spread."
    )

    logger.info(f"Random sandwich: {sandwich}")
    logger.info("")


# String Lists 3. Get Unique Words

def process_text_zen_of_python():
    """Read in text_zen_of_python.txt and process it"""
    logger.info("String Lists 3. Get Unique Words")
    logger.info("Calling process_text_zen_of_python()")

    # read in zen_of_python to get a list of words
    with open("text_zen_of_python.txt", "r") as fileObject:
        text = fileObject.read()
        list_words = text.split()  # split on whitespace
        unique_words = set(list_words)  # remove duplicates by making a set

        # Get the count and list of words
        word_ct = len(list_words)

        logger.info(f"The list of words is: {list_words}")
        logger.info(f"There are {word_ct} words in the file.")

        # Print the count and list of unique words
        unique_word_ct = len(unique_words)

        logger.info(f"The set of unique words is: {unique_words}")
        logger.info(f"There are {unique_word_ct} unique words in the file.")

        # Sort the list
        word_sort = sorted(list_words)

        logger.info(f"Here is the sorted list: {word_sort}")




def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())


# -------------------------------------------------------------
# Call some functions and execute code!
# Remember, code blocks must be indented consistently after a colon.

if __name__ == "__main__":
    logger.info("Calling functions from main block")

    menu_info()
    menu_built_in_funtctions()
    create_random_sandwiches()
    create_random_sandwiches()
    create_random_sandwiches()
    create_random_sandwiches()
    process_text_zen_of_python()
  
    show_log()