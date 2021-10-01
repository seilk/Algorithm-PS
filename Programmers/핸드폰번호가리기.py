# import re
# x = "11111111"
# print(type(x[:-4]))
# y = x.replace(x[:-4], "*" * len(x[:-4]), 1)
# print(y)
# https://note.nkmk.me/en/python-str-replace-translate-re-sub/

import re


def solution(p):
    private = p.replace(p[:-4], "*" * len(p[:-4]), 1)
    return private


def hide_numbers(s):
    p = re.compile(r'\d(?=\d{4})')
    return p.sub("*", s, count=0)
