#!/usr/bin/python3
""" module that allows text manuplation"""


def text_indentation(text):
    """unction that prints a text with 2 new lines after each of
    these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    for t in range(len(text)):
        if text[t] == " " and (not result or result[-1] == '\n'):
            continue
        if text[t] == "\n":
            while result and result[-1] == ' ':
                result = result[:-1]
            result += "\n"
            continue
        if t == len(text) - 1 and result[-1] == ' ' and text[t] == " ":
            while result and result[-1] == ' ':
                result = result[:-1]
            continue
        if text[t] in ".?:":
            result += text[t]
            result += "\n\n"
        else:
            result += text[t]
    print(result, end="")
