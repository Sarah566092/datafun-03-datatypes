"""
Examples of Numeric Lists Using the Domain of Food

Author: Sarah DeConink

In this script we will look at Statistics, Correlation and Prediction, Using built-in functions, Methods,
Transformations using filter() and map(), and Transformations using List Comprehension

"""

# import some modules first - how many can you make use of?
import statistics
import math

from util_datafun_logger import setup_logger
logger,logname = setup_logger(__file__)


# Create list1 - a list of the daily # of customer reviews for Sarah's Sammie Shoppe in July
list1 = [
    20,
    35,
    54,
    0,
    17,
    47,
    11,
    67,
    80,
    33,
    44,
    78,
    17,
    47,
    0,
    50,
    17,
    17,
    35,
    47,
    31,
    75,
    17,
    25,
    44,
    17,
    62,
    65,
    77,
    56,
    68
]


# listx represents the first 10 days the shop is open, listy represents the number of paninis that were made each day
listx = list(range(10))
listy = [5, 11, 14, 19, 25, 31, 37, 42, 47, 51]



# Lists 1 - Calculate Descriptive stats

# Measures of central tendency
mean = statistics.mean(list1)
median = statistics.median(list1)
mode = statistics.mode(list1)

# Measures of spread
stdev = statistics.stdev(list1)
variance = statistics.variance(list1)




# Lists 2 - Correlation and Prediction

# Measures of correlation
correlationxy = statistics.correlation(listx, listy)

# Find a slope and intercept of the x,y values using linear regression
slope, intercept = statistics.linear_regression(listx, listy)

# Choose a future x value and predict a y value
x_future = 15
predict_y = slope * x_future + intercept



# Lists 3 - Use Python Buit-in Functions

# Using the list of customer reviews per day in July provided above, do the following:
# Calcuate the max and min review
max = max(list1)
min = min(list1)

# Calculate the length of the list
len = len(list1)

# Calculate the sum of the list
sum = sum(list1)

# Calculate the average of the list
avg = sum / len

# Make a set from the list - no repeated values
set = set(list1)

# Return a new list soreted in ascending order
asc_list1 = sorted(list1)

# Return a new list soreted in descending order
desc_list1 = sorted(list1, reverse=True)

# Print Values for Python Built-in Functions




# Lists 4 - Methods

# append an item to the end of the list of $ in the tips jar for Sarah's Sammie Shoppe
lst = [2, 4, 2, 6]
start_lst = lst
append_lst = lst.append(5)


# extend the list with another list
lst.extend([2, 4, 5, 8])
extend_lst = lst

# insert an item at a given position (0 = first item)
i = 0
newvalue = 10
lst.insert(i, newvalue)
insert_lst = lst

# remove an item
item_to_remove = 5
lst.remove(item_to_remove)
remove_item = lst

# Count how many times 2 appears in the list
ct_of_2 = lst.count(2)

# Copy the list to a new list
original_lst = lst.copy()

# Remove the first item from the new list
first = lst.pop(0)

# Remove the last item from the new list
last = lst.pop(-1)

# Sort the list in ascending order using the sort() method
original_lst.sort()
list_sort_asc = original_lst

# Sort the list in descending order using the sort() method
original_lst.sort(reverse=True)
list_sort_desc = original_lst



# Lists 5 - Transformations using filter() and map()

new_lst = original_lst.copy()

tips_over_4 = list(filter(lambda x: x > 4, new_lst))

# Use the built-in function map() anywhere you need to transfrom

# Map each element to its cubed root
cubed_root_lst = list(map(lambda x: math.cbrt(x), new_lst))

# Map each element (cube side) to its volume
side_list = [3, 4, 5]
# Say "map r to pi r squared" and cast to a list
volume_list = list(map(lambda s: s * s * s, side_list))



# Lists 6 Transformations unsing List Comprehension

# Find the # of reviews that there were less than 50 reviews
reviews_under_50 = [x for x in list1 if x < 50]

# Map each # of reviews to be triple
triple_reviews = [x * 3 for x in list1]

# Map each # of reviews to be quadrupled
quad_reviews = [x * 4 for x in list1]



# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    logger.info("Numerical Lists for Sarah's Sammie Shoppe")
    logger.info("")
    logger.info("Lists 1 - Statistics Customer Reviews in July")
    logger.info(f"Here is a list of the daily # of customer reviews for Sarah's Sammie Shoppe in July: {list1}")
    logger.info(f"There were a total of {len} days of data provided.")
    logger.info(f"The mean of the # of reviews is {mean:.2f}.")
    logger.info(f"The median of the # of reviews is {median}.")
    logger.info(f"The mode of the # of reviews is {mode}.")
    logger.info(f"The standard deviation of the # of reviews is {stdev:.2f}.")
    logger.info(f"The variance of the # of reviews is {variance:.2f}.")
    logger.info("")
    logger.info("Lists 2 - Correlation and Prediction")
    logger.info(f"The the first {listx} days of business Sarah's Sammie Shoppe sold {listy} paninis.")
    logger.info(f"The correlation of the first ten days of business and the number of paninis sold is {correlationxy:.2f}.")
    logger.info(f"The slope (sales per day) is {slope:.2f}.")
    logger.info(f"The intercept (starting # of sales) is {intercept:.2f}.")
    logger.info(f"On Day {x_future} of our business, we predict we will sell {predict_y:.2f} paninis.")
    logger.info("")
    logger.info("Lists 3 - Using Python built-in functions")
    logger.info(f"The lowest # of reviews is {min}.")
    logger.info(f"The highest # of reviews is {max}.")
    logger.info(f"The sum of the # of reviews is {sum}.")
    logger.info(f"The average of the # of reviews is {avg:.2f}.")
    logger.info(f"The # of reviews without repeats: {set}.")
    logger.info(f"The # of reviews from lowest to highest: {asc_list1}.")
    logger.info(f"The # of reviews from highest to lowest {desc_list1}.")
    logger.info("")
    logger.info("Lists 4 - List Methods")
    logger.info(f"Here is a list of some tips at Sarah's Sammie Shoppe: {start_lst}")
    logger.info(f"Append the list with a $5 tip: {append_lst}")
    logger.info(f"Customers are generous today. Extend the list with $2, $4, $5, $8 tips: {extend_lst}")
    logger.info(f"Add one tip we forgot to count at the bottom of the jar: {insert_lst}")
    logger.info(f"What! A kid just stole a $5 bill from the jar! Here is the new list: {remove_item}")
    logger.info(f"Here is a copy of the original list: {original_lst}")
    logger.info(f"Here are the tips ordered lowest to highest: {list_sort_asc}")
    logger.info(f"Here are the tips ordered highest to lowest: {list_sort_desc}")
    logger.info(f"There were {ct_of_2} $2 tips today.")
    logger.info(f"The first tip of the day was: ${first}")
    logger.info(f"The last tip of the day was: ${last}")
    logger.info("")
    logger.info("Lists 5 - Transformations using filter() and map()")
    logger.info("Strange facts about the tips")
    logger.info(f"Here are the tips that were over $4: {tips_over_4}")
    logger.info(f"Here is the cubed root of the tips. This is losing meaning!: {cubed_root_lst}")
    logger.info(f"Here are the volumes of boxes available to hold tomorrow's tips: {volume_list}")
    logger.info("")
    logger.info("Lists 6 - Transformations using List Comprehension")
    logger.info("Back to our customer surveys")
    logger.info(f"Here are # of reviews per day that were less than 50: {reviews_under_50}")
    logger.info(f"Here are is our goal of tripling our daily reviews by October: {triple_reviews}")
    logger.info(f"Here are is our goal of quadrupling our daily reviews by December: {quad_reviews}")




# Why? Why only print if this the module called?
# Because when you write good functions, you may want to
# import this module into another script - just like you did
# math or statistics.
# Build a library of resuable functions to support your domain.

# For example, if your domain:
# Is sports, create functions to provide a list of teams.
# Is pets, create functions to calculate adoption prices.
# Is music, create functions to return a list of your favorite artists.


# When you write reusable functions for your domain, you can
# import the module with your utility functions into other modules
# and use them there.  This is a very common practice.
# Anything you write can be imported into later projects.

