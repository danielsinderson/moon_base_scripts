"""
A script for generating flash fiction prompts from tracery grammars
"""

import tracery, random

grammars: dict  ={

}

def generate_setting() -> str:
    result: str = ""
    return result


def generate_story() -> str:
    result: str = ""
    return result


def generate_constraints() -> list:
    selector: bool = random.choice([True, False])
    perspective = "First-Person" if selector else "Second-Person"
    
    quirks = [
        "Use every letter in the alphabet at least once",
        "Completely avoid a vowel of your choice",
        "Don't use any commas",
        "Write the entire piece as one sentence",
        "Write the entire piece as a dialogue",
        "Weave in something from the first random [Wikipedia](https://en.wikipedia.org/wiki/Special:Random) article you see",
        "Include at least three made up slang words",
    ]
    quirk = random.choice(quirks)
    
    word_limit = f"{random.randint(1, 10) * 250} words"
    
    result = [perspective, quirk, word_limit]
    return result


def generate_prompt() -> str:
    setting: str = generate_setting()
    story: str = generate_story()
    
    constraints: list = generate_constraints()
    perspective: str = constraints[0]
    quirk: str = constraints[1]
    word_limit: str = constraints[2]
    
    result: str = f"""
    SETTING: {setting}\n
    STORY: {story}\n
    PERSPECTIVE: {perspective}\n
    OPTIONAL QUIRK: {quirk}\n
    WORD LIMIT: {word_limit}\n
    """
    return result


def main():
    prompt: str = generate_prompt()
    print(prompt)


if __name__ == "__main__":
    main()