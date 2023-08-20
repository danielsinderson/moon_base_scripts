"""
A script for generating flash fiction prompts from tracery grammars
"""

import tracery, random


def generate_setting() -> str:
    result: str = ""
    return result


def generate_story() -> str:
    result: str = ""
    return result


def generate_constraints() -> list:
    result: str = ""
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