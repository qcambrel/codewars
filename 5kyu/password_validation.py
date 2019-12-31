# KATA: Regex Password Validation
# https://www.codewars.com/kata/52e1476c8147a7547a000811/train/python

# You need to write regex that will validate a password to make sure it meets the following criteria:

# - at least six characters long
# - contains a lowercase letter
# - contains an uppercase letter
# - contains a number
# Valid passwords will only be alphanumeric characters.


regex = "^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])[A-Za-z\d]{6,}$"

# ?=.*? creates what is called a positive lookahead 
# without it, the regex would validate passwords such as 456789 or AAAAAA
# positive lookahead states that at least one character from each set must be used
