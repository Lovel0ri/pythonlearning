# @Time: 2022/11/25 11:39
# @Author: 李树斌
# @File : vsearch.py
# @Software :PyCharm


def search4letters(phrase: str, letters: str) -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))

