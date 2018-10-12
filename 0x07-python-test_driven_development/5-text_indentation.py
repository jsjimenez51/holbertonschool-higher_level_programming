#!/usr/bin/python3
"""
This module identifies specific characters in text then prints 2 newlines
following the character.
"""


def text_indentation(text):
    """
    Function to print text read and insert 2 newlines after one of the
    specified characters is found: - . ?
    """
    if not isinstance(text, str) or len(text) < 0 or text is None:
        raise TypeError('text must be a string')
    line = "".join([ltr if ltr not in ".?:" else ltr + "\n\n" for ltr in text])
    print("\n".join([string.strip() for string in line.split("\n")]), end="")
