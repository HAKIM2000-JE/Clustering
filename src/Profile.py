# Use Python's built-in datetime module
from datetime import date, datetime
from kmeans_numpy_improved import *

def age(birthdate):

    birthdate =datetime.strptime(birthdate, '%Y-%m-%d')
    # Get today's date object
    today = date.today()

    # A bool that represents if today's day/month precedes the birth day/month
    one_or_zero = ((today.month, today.day) < (birthdate.month, birthdate.day))

    # Calculate the difference in years from the date object's components
    year_difference = today.year - birthdate.year

    # The difference in years is not enough.
    # To get it right, subtract 1 or 0 based on if today precedes the
    # birthdate's month/day.

    # To do this, subtract the 'one_or_zero' boolean
    # from 'year_difference'. (This converts
    # True to 1 and False to 0 under the hood.)
    age = year_difference - one_or_zero

    return age


  #function that calculate similarities between the new guest and other created profiles
def jaccard_binary(x, y):
        """A function for finding the similarity between two binary vectors"""
        intersection = np.logical_and(x, y)
        union = np.logical_or(x, y)
        similarity = intersection.sum() / float(union.sum())
        return similarity


