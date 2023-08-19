"""
This is a script that takes a poem and subjects it to a battery of tests.
The tests are pulled from the "Nuts and Bolts" section of "The Triggering Town" by Richard Hugo.

The returned result is a report of which tests passed, and which failed and where.

input: str
output: str

tests:
1) Avoid using "love" as an intransitive verb
2) End half or more of your sentences on a one syllable word
3) Avoid the verb "to be"
4) Max sentence length 17 words
5) Each sentence should be four, or more, words longer or shorter than the sentence prior 
6) Avoid clarifying words [while, meanwhile, during, so, because, thus, causing, yet, but]
7) Keep your subject close to the front of the sentence
8) Use more concrete nouns than abstract ones
"""

import spacy


def love_as_intransitive(text: str) -> tuple[bool, int, list]:
    passed: bool
    num_used: int
    where_used: list[str]
    
    result = (passed, num_used, where_used)
    return result


def sentence_endings(text: str) -> tuple[bool, float, list]:
    passed: bool
    ratio: float
    endings: list[str]
    
    result = (passed, ratio, endings)
    return result


def avoid_to_be(text: str) -> tuple[int, list]:
    num_used: int
    where_used: list
    
    result = (num_used, where_used)
    return result


def max_sentence_length(text: str) -> tuple[bool, int]:
    passed: bool
    actual_max: int
    
    result = (passed, actual_max)
    return result


def sentence_variability(text: str) -> tuple[bool, list]:
    passed: bool
    where_failed: list[str]
    
    result = (passed, where_failed)
    return result


def avoid_clarifying_words(text: str) -> tuple[int, list]:
    num_used: int
    where_used: list[str]
    
    result = (num_used, where_used)
    return result


def subject_near_beginning(text: str) -> tuple[float, list]:
    ratio: float
    where_failed: list[str]
    
    result = (ratio, where_failed)
    return result


def abstract_nouns(text: str) -> tuple[float, list]:
    ratio: float
    where_used: list[str]
    
    result = (ratio, where_used)
    return result


def main():
    pass


if __name__ == "__main__":
    main()
    