regex = "^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])[A-Za-z\d]{6,}$"

# ?=.*? creates what is called a positive lookahead 
# without it, the regex would validate passwords such as 456789 or AAAAAA
# positive lookahead states that at least one character from each set must be used
