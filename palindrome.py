"""
PROBLEM STATEMENT [2]

Write a function that checks if a given word is a palindrome. Character case should be ignored.

"""

def is_palindrome(word):
    word = word.lower()
    reversed_string = ''.join(reversed(word)) # inBuilt Reversed Funtion

    if word == reversed_string:
        return True
    return False  

print(is_palindrome('Radar'))