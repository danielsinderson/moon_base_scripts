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
        where_used.append(f"SENTENCE {index + 1}: " + sentence.replace("\n\n", " // ").replace("\n", " / "))
    
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
    num_used: int = 0
    where_used: list = []
    
    words_to_avoid = [
        "am",
        "was",
        "are",
        "is",
        "were"
    ]
    
    # clean up the contractions
    text = text.replace("e's", "e is").replace("t's", "t is")
    text = text.replace("n't", " not").replace("'m", " am").replace("'re", " are")
    
    # split into lines then into words and loop over them
    lines = text.split("\n")
    for index, line in enumerate(lines):
        words = line.split(" ")
        for word in words:
            # check to see if those words are in our words_to_avoid list
            if word in words_to_avoid:
                num_used += 1
                where_used.append(f"LINE {index + 1}: " + line)
    
    result = ""
    passed: bool = (num_used <= int(len(lines) / 3))
    if passed:
        result = f"The Verb to Be Test passed! You used it only {num_used} times across {len(lines)} lines."
    else: 
        result = f"The Verb to Be Test failed. You used it {num_used} times across {len(lines)} lines. Consider the following lines to see if it could be removed or replaced:\n- " + "\n- ".join(where_used)
    
    #print(result)
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
    passed: bool = True
    num_used: int = 0
    where_used: list = []
    
    words_to_avoid = [
        "while",
        "meanwhile",
        "as",
        "during",
        "so",
        "because",
        "thus",
        "causing",
        "yet",
        "but"
    ]
    
    # split into lines then into words and loop over them
    lines = text.split("\n")
    for index, line in enumerate(lines):
        words = line.split(" ")
        for word in words:
            # check to see if those words are in our words_to_avoid list
            if word in words_to_avoid:
                num_used += 1
                where_used.append(f"LINE {index + 1}: " + line)
                passed = False
    
    result = ""
    if passed:
        result = f"The Clarifying Words Test passed! You didn't use any of them."
    else: 
        result = f"The Clarifying Words Test failed. You used them {num_used} times across {len(lines)} lines. Consider the following lines to see if they could be removed or replaced:\n- " + "\n- ".join(where_used)
    
    print(result)
    return result


def test_text(text: str) -> str:
    test1: str = love_as_intransitive(text)
    #test2: str = sentence_endings(text)
    test3: str = avoid_to_be(text)
    #test4: str = max_sentence_length(text)
    #test5: str = sentence_variability(text)
    test6: str = avoid_clarifying_words(text)

    


def main():
    test_text("This is a test. Don't\nlook too hard\nat the things it says.\n\nIt can't hurt you. It can't\neven say its own name\nyet. I love you. But love \n is not\n\neverything. I was\na bird before this. I was\ndead there.")


if __name__ == "__main__":
    main()
    