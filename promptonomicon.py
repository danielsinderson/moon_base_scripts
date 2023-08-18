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
    word_lists = {}
    return word_lists


def generate_structure() -> dict:
    structure = {}
    return structure


def generate_sonic_constraint(structure: dict) -> str:
    sonic_constraint = ""
    return sonic_constraint


def generate_end_stop_constraint(structure: dict) -> str:
    end_stop_constraint = ""
    return end_stop_constraint


def generate_quirk() -> str:
    quirk = ""
    return quirk


def format_prompt(word_lists: dict,
                  structure: dict,
                  sonic_constraint: str,
                  end_stop_constraint: str,
                  quirk: str
                  ) -> str:
    formatted_prompt = ""
    return formatted_prompt


def generate_prompt() -> str:
    word_lists: dict = generate_word_lists()
    structure: dict = generate_structure()
    sonic_constraint: str = generate_sonic_constraint(structure=structure)
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