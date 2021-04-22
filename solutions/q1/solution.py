from collections import Counter
from typing import Dict
import logging


def check_anagram():
    """
    Checks whether the strings are anagram. If they are not calculates minimum number of character deletions required to
    make the two strings anagrams.
    """
    print("a: ", end='')
    first_string = input()
    print("b: ", end='')
    sec_string = input()
    if sorted(first_string) == sorted(sec_string):
        print("they are anagrams")
    else:
        remove_first = 0
        remove_second = 0
        unique_chars = set(first_string + sec_string)
        first_char_freq: Dict[str, int] = Counter(first_string)
        sec_char_freq: Dict[str, int] = Counter(sec_string)
        for char in unique_chars:
            if char in first_char_freq:
                if char in sec_char_freq:
                    if first_char_freq[char] != sec_char_freq[char]:  # todo bu if'i yukarimi alsan
                        diff = abs(first_char_freq[char] - sec_char_freq[char])
                        if first_char_freq[char] > sec_char_freq[char]:
                            remove_first += diff
                        else:
                            remove_second += diff
                else:
                    remove_first += first_char_freq[char]
            else:
                remove_second += sec_char_freq[char]
        print("remove {0} characters from '{1}' and {2} characters from '{3}'".format(remove_first, first_string,
                                                                                      remove_second, sec_string))


if __name__ == '__main__':
    try:
        check_anagram()
    except Exception as ex:
        logging.error("An error occured ==> {0}".format(ex))
