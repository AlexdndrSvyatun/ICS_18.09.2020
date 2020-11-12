import csv
import sys

import collections

c = collections.Counter()

class StringChild(str):
    def is_sequence(self, s):
        for i, char in enumerate(s):
            if(i <= len(s)-2):
                if(char == s[i+1] and char == s[i+2]):
                    return True
        return False

    def is_palindrome(self, raw):
        if(raw == ''):
            return True

        reverse_raw = raw[::-1]

        if reverse_raw.lower() == raw.lower():
            return True
        else:
            return False

my_str = StringChild()

s1 = input('введіть рядок для перевірки на наявність послідовності  символів що повторюються: ')
print(my_str.is_sequence(s1))
print('\n')
s2 = input('введіть ваш рядок для перевірки на паліндромність: ')
print(my_str.is_palindrome(s2))