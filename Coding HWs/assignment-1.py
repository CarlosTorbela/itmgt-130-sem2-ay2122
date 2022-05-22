'''Assignment 1
This assignment covers your basic profiency with
    Python. It engages your ability to transform
    data without affecting anything outside the program.
This assignment places heavy emphasis on basic Python constructs.
'''

def factorial(x):
    '''Item 1. 
    Factorial. 1 point.
    
    Returns the factorial of an integer.
    An integer's factorial is the product of the integer and all
        integers below it.
    Parameters
    ----------
    x: int
        the integer whose factorial to return
    Returns
    -------
    integer
        the factorial of the argument
    '''
    # Write your code below this line
    factorial = 1
    if x >= 1:
        for i in range (1, x+1):
            factorial = factorial * i
    return factorial

def classify_grade(number_grade):
    '''Item 2.
    Classify Grade. 2 points.
    
    Returns the letter grade equivalent of a number grade.
    For this item, use these letter grade buckets:
        A: 92-100
        B+: 86-91.9
        B: 80-85.9
        C+: 74-79.9
        C: 67-73.9
        D: 60-66.9
        F: 0-59.9
    Parameters
    ----------
    number_grade: float
        the number grade to convert into a letter grade.
    Returns
    -------
    str
        the letter grade equivalent of the number grade.
    '''
    # Write your code below this line
    if number_grade >= 92 and number_grade <= 100:
        return "A"
    elif number_grade >= 86 and number_grade <= 91.9:
        return "B+"
    elif number_grade >= 80 and number_grade <= 85.9:
        return "B"
    elif number_grade >= 74 and number_grade <= 79.9:
        return "C+"
    elif number_grade >= 67 and number_grade <= 73.9:
        return "C"
    elif number_grade >= 60 and number_grade <= 66.9:
        return "D"
    elif number_grade >= 0 and number_grade <= 59.9:
        return "F"
    return "invalid number grade"

def average_weight(item_quantity_1, item_weight_1, item_quantity_2, item_weight_2):
    '''Item 3.
    Average Weight. 3 points.
    
    You have purchased two bags of items. 
    The first bag contains one type of item, and the second bag contains another type.
    Return the weighted average weight of the items.
        
    Parameters
    ----------
    item_quantity_1: int
        the quantity of items in the first bag.
    item_weight_1: float
        the weight of each individual item in the first bag.
    item_quantity_2: int
        the quantity of items in the second bag.
    item_weight_2: float
        the weight of each individual item in the second bag.
    Returns
    -------
    float
        the weighted average weight of one item.
    '''
    # Write your code below this line
    total_quantity = item_quantity_1 + item_quantity_2
    x = item_quantity_1 * item_weight_1
    y = item_quantity_2 * item_weight_2
    total = x + y
    average_weight = total / total_quantity
    return average_weight

def string_sum(string):
    '''Item 4.
    String Sum. 3 points.
    
    Returns the sum of the digits provided in a string.
    For this item:
        1. Sum the digits contained in the string.
        2. Ignore any non-digit characters contained in the string.
    Parameters
    ----------
    string: str
        a string that can contain any character.
    Returns
    -------
    int
        the sum of the digits contained in the string.
    '''
    # Write your code below this line
    sum = 0
    for char in string:
        if(char >= '0' and char <= '9'):
            sum += int(char)
    return sum

import math
def distance(x_1, y_1, x_2, y_2):
    '''Item 5.
    Distance. 3 points.
    Returns the distance between two points.
    To get the distance between two points:
        1. Get the difference between the two x-coordinates
        2. Get the difference between the two y-coordinates
        3. Sum the previous two values
        4. Return the square root of the sum
    You may want to import the `math` library for this number.
    Parameters
    ----------
    x_1: float
        the first x-coordinate
    y_1: float
        the first y-coordinate
    x_2: float
        the second x-coordinate
    y_2: float
        the second y-coordinate
    Returns
    -------
    float
        the distance between the two coordinates
    '''
    # Write your code below this line
    # x_distance = 0
    # y_distance = 0
    if x_1 > x_2:
        x_distance = x_1 - x_2
    else:
        x_distance = x_2 - x_1 
    if y_1 > y_2:
        y_distance = y_1 - y_2
    else:
        y_distance = y_2 - y_1
    final_distance = math.sqrt(x_distance + y_distance)
    return final_distance

def make_change(amount):
    '''Item 6.
    Make Change. 5 points.
    
    Return the combination of coins needed to make change for the given amount,
        which is given in centavos.
    For this item:
        1. You can return 1 peso, 25 centavos, 10 centavos, 5 centavos, and 1 centavo coins.
        2. Use the minimum number of coins possible.
    Parameters
    ----------
    amount: int
        the amount, in centavos, to make change for.
    Returns
    -------
    str
        the string representation of the change to be given.
        Format it like this:
            "1P:{amount}/25C:{amount}/10C:{amount}/5C:{amount}/1C:{amount}"
    '''
    # Write your code below this line
    one_peso = 0
    twenty_five_centavos = 0
    ten_centavos = 0
    five_centavos = 0
    one_centavo = 0
    while amount != 0:
        if amount / 100 >= 1:
            one_peso = int((amount / 100))
            amount = amount % 100
        if amount / 25 >= 1:     
            twenty_five_centavos = int((amount / 25))
            amount = amount % 25
        if amount / 10 >= 1:
            ten_centavos = int((amount / 10))
            amount = amount % 10    
        if amount / 5 >= 1:
            five_centavos = int((amount / 5))
            amount = amount % 5
        if amount / 1 >= 1:
            one_centavo = int((amount / 1))
            amount = amount % 1
    return(f"1P:{one_peso}/25C:{twenty_five_centavos}/10C:{ten_centavos}/5C:{five_centavos}/1C:{one_centavo}")