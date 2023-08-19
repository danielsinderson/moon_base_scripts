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
"""

import re


def love_as_intransitive(text: str) -> str:
    passed: bool = True
    num_used: int = 0
    where_used: list = []
    result: str = ""
    
    sentences = re.split(r"[\.\?\!]", text)
    love_pattern = r"(?:i|you|he|she|they|we|it)\slove\s(?:me|you|him|her|them|us|it)"
    
    for index, sentence in enumerate(sentences):
        transitive_loves = len(re.findall(love_pattern, sentence.lower()))
        total_loves = len(re.findall(r"love", sentence))
        if transitive_loves == total_loves:
            continue
        num_used += 1
        passed = False
        where_used.append(f"SENTENCE {index}: " + sentence.replace("\n\n", " // ").replace("\n", " / "))
    
    if passed:
        result = "The Love as Intransitive Verb Test passed!"
    else:
        result = f"The Love as Intransitive Verb Test failed {num_used} {'time' if num_used == 1 else 'times'}. Double check that each of the following usages are truly necessary:\n- " + "\n- ".join(where_used)
    
    #print(result)
    return result


def sentence_endings(text: str) -> str:
    passed: bool
    ratio: float
    endings: list[str]
    
    result = (passed, ratio, endings)
    return result


def avoid_to_be(text: str) -> str:
    num_used: int
    where_used: list
    
    result = (num_used, where_used)
    return result


def max_sentence_length(text: str) -> str:
    passed: bool
    actual_max: int
    
    result = (passed, actual_max)
    return result


def sentence_variability(text: str) -> str:
    passed: bool
    where_failed: list[str]
    
    result = (passed, where_failed)
    return result


def avoid_clarifying_words(text: str) -> str:
    num_used: int
    where_used: list[str]
    
    result = (num_used, where_used)
    return result


def test_text(text: str) -> str:
    test1: str = love_as_intransitive(text)
    #test2: str = sentence_endings(text)
    #test3: str = avoid_to_be(text)
    #test4: str = max_sentence_length(text)
    #test5: str = sentence_variability(text)
    #test6: str = avoid_clarifying_words(text)

    


def main():
    test_text("This is for testing\npurposes. Don't look too hard\nat the things it says.\n\nIt can't hurt you. It can't\neven say its own name\nyet. I love you. But love \n is not enough.")


if __name__ == "__main__":
    main()
    