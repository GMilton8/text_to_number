# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 15:22:28 2021

@author: gmilt
"""
import re

# Program to retrieve a number from an input and to output that number in 
# word format.
# The logic behind the code is as follows: search the input for a number and convert
# to an integer. Then, consider this integer 3 digits at a time, starting from units 
# to tens, to hundreds and so forth.
# If there is just one set of 3 (ie number <= 999), stop. If multiple sets of 3,
# then repeat the previous step, adding in the correct qualifying word, be that
# thousands, millions or billions etc



# Input the text of your choice as a string
input = 'The database has 66723107008 records.'


# Defines a dictionary list for number 1 - 19, given the pronunciations of these
words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
            19: 'Nineteen', 0: ''}

# Dictionary for the tens
tens = {2: 'Twenty', 3: 'Thirty', 4: 'Fourty', 5: 'Fifty', \
             6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}
     
# Finds first number from the input
number = re.findall(r'\d+', input)
y = number[0]

y1 = int(y[-2:]) # selects the last two numbers and converts to an integer

# sets up empty strings, to be used in the thousands / millions / billions steps
b = ""
c = ""
d = ""
e = ""
f = ""
g = ""
k = ""

# If last two digits less than 20, word selected from 1-19 dictionary
if y1 < 20:
    a = words[y1]    
else:
    a1 = tens[int(y[-2:-1])] # first digit of the two assigned to the tens
    a2 = words[int(y[-1:])]  # second digit assigned to the initial set
    a = a1 + " " + a2        # final variable is combo of tens and units
    
# If the third digit is non-zero, identify it and add 'hundred' word
if len(y) > 2:
    if words[int(y[-3:-2])] == "": # "" corresponds to zero in the dictionary
        b = ""
    else:
        b1 = words[int(y[-3:-2])] # determines hundreds value
# below line deals with numbers with multiple zeroes in front, in order to avoid
# the inclusion of 'hundred' if there aren't any, eg for 10,000
        if b1 == "": 
            b = "" 
        else:
            b = b1 + " Hundred "
    
# Considers the next set of 3 numbers and repeats a similar process to above
if len(y) > 3:
    p = int(y[:len(y)-3]) # selects the number minus the final 3 digits
    q = str(p)[-3:] # takes the final 3 digits of p 
    y2 = int(q[-2:]) # selects the last two numbers and converts to an integer
    if y2 < 20:
        c = words[y2]    
    else:
        c1 = tens[int(q[-2:-1])] # first digit assigned to the tens
        c2 = words[int(q[-1:])]  # second digit assigned to the initial set
        c = c1 + " " + c2 
       
    if len(q) > 2:
        d1 = words[int(q[-3:-2])] # determines hundreds value
        d = d1 + " Hundred"
        if d1 == "":
            d = ""
    else:
        d1 = ""  # code to deal with zeroes in front, as described above
        d = ""

if ( c == "" and d ==""): # condition to skip the thousand if 0
    e = ""
else:
    e = d + " " + c + " Thousand and "
    
# From here below, the above code is repeated and varied slightly to refelect
# millions instead of thousands    
    
if len(y) > 6:
    r = int(y[:len(y)-6]) # selects the number minus the final 6 digits
    s = str(r)[-3:] # takes the final 3 digits of r 
    y3 = int(s[-2:]) # selects the last two numbers and converts to an integer
    if y3 < 20:
        f = words[y3]    
    else:
        f1 = tens[int(s[-2:-1])] # first digit assigned to the tens
        f2 = words[int(s[-1:])]  # second digit assigned to the initial set
        f = f1 + " " + f2 
    
    if len(s) > 2:
        g1 = words[int(s[-3:-2])] # determines hundreds value
        g = g1 + " Hundred and"
        if g1 == "":
            g = ""
    else:
        g1 = ""
        g = ""

if ( g == "" and f == ""):
    g = ""    
else:
    g = g + " " + f + " Million " # condition to skip the million if 0

# again, repeated for billions rather than millions

if len(y) > 9:
    t = int(y[:len(y)-9]) # selects the number minus the final 9 digits
    u = str(t)[-3:] # takes the final 3 digits of t 
    y4 = int(u[-2:]) # selects the last two numbers and converts to an integer
    if y4 < 20:
        h = words[y4]    
    else:
        h1 = tens[int(u[-2:-1])] # first digit assigned to the tens
        h2 = words[int(u[-1:])]  # second digit assigned to the initial set
        h = h1 + " " + h2 
    
    if len(u) > 2:
        k1 = words[int(u[-3:-2])] # determines hundreds value
        k = k1 + " Hundred and"
    else:
        k1 = ""
        k = ""

        
    k = k + " " + h + " Billion "

# Output is the combination of the words for each group of 3 numbers considered
STDOUT = k + g + e + b + a
print(STDOUT)


