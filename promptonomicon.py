"""
A script to quickly create a prompt for poems.
Generated prompts are based on the exercise outlined in "The Triggering Town" by Richard Hugo:

1) Generate lists of 10 nouns, 10 adjectives, and 10 verbs, of which five of each must be used
2) Generate structure: 2-10 lines per stanza, 1-10 stanzas, no less than 2 lines no more than 30 lines per poem
3) Generate sonic constraint: 1-3 slant rhymes (internal or external) or alliterations per stanza
4) Max of 1-(3/4 * line total) total end stops
5) Generate additional quirk
"""

import random


def generate_word_lists() -> dict:
    word_lists = {
        "nouns": [],
        "adjectives": [],
        "verbs": []
    }
    return word_lists


def generate_structure() -> dict:
    lines_per_stanza = random.randint(2, 5)
    stanzas = random.randint(1, 5)
    
    structure = {
        "lines_per_stanza": lines_per_stanza,
        "stanzas": stanzas,
        "total_lines": lines_per_stanza * stanzas
    }
    return structure


def generate_sonic_constraint() -> str:
    types_of_constraint = [
        "internal slant rhyme",
        "external slant rhyme",
        "alliteration",
        "consonant pair",
        "assonant pair"
    ]
    
    count = random.choice(["one", "two"])
    
    constraint = random.choice(types_of_constraint)
    if count == "two":
        constraint += "s"
    
    sonic_constraint = f"at least {count} {constraint} per stanza."
    
    return sonic_constraint


def generate_end_stop_constraint(structure: dict) -> str:
    max_end_stops = random.randint(2, int(structure["total_lines"] / 2))
    end_stop_constraint = f"no more than {max_end_stops} end stops."
    return end_stop_constraint


def generate_quirk() -> str:
    quirks = [
        "must have an epigraph you've made up yourself.",
        "must follow a consistent meter.",
        "must be an acrostic.",
        "must use only two kinds of punctuation max.",
        "must not use one of the vowels.",
        "must only use 10 consonants.",
        "must use every consonant at least once.",
        "must have a consistent syllable count for every line."
    ]
    quirk = ""
    if random.randint(0, 1):
        quirk = random.choice(quirks)
    return quirk


def format_prompt(word_lists: dict,
                  structure: dict,
                  sonic_constraint: str,
                  end_stop_constraint: str,
                  quirk: str
                  ) -> str:
    formatted_prompt = f"""
    Your poem must adhere to the following constraints:\n
    1. It must contain {structure['stanzas']} stanzas.\n
    2. There must be {structure['lines_per_stanza']} lines per stanza.\n
    3. It must have {sonic_constraint}\n
    4. It must contain {end_stop_constraint}\n
    5. It must choose a noun, an adjective, and a verb from the following lists for every stanza\n
    \n
    Nouns: {word_lists["nouns"]}\n
    Adjectives: {word_lists["adjectives"]}\n
    Verbs: {word_lists["verbs"]}\n
    """
    
    if quirk != "":
        formatted_prompt += f"\n\nAnd, as an added challenge, it {quirk}"
        
    formatted_prompt += "\n\nGood luck!"
    return formatted_prompt


def generate_prompt() -> str:
    word_lists: dict = generate_word_lists()
    structure: dict = generate_structure()
    sonic_constraint: str = generate_sonic_constraint()
    end_stop_constraint: str = generate_end_stop_constraint(structure=structure)
    quirk = generate_quirk() if random.randint(0, 1) else ""
    
    prompt = format_prompt(word_lists=word_lists,
                           structure=structure,
                           sonic_constraint=sonic_constraint,
                           end_stop_constraint=end_stop_constraint,
                           quirk=quirk
                           )
    return prompt


def main():
    prompt: str = generate_prompt()
    print(prompt)


if __name__ == "__main__":
    main()