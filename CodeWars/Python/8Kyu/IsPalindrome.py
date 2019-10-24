# Link = https://www.codewars.com/kata/is-it-a-palindrome

import unittest

def is_palindrome(s):
    if ''.join(list(reversed(s.lower()))) == s.lower():
        return True
    else:
        return False

