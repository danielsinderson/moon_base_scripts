"""
A script for generating flash fiction prompts from tracery grammars
"""

import tracery, random
from tracery.modifiers import base_english


rules = {
    "story": [
        "#subject.a# #transitive_verb#",
    ],
    "subject": ["#person#", "#occupation#"],
    "person": ["teenager", "kid", "boy", "girl", "man", "woman", "old man", "old woman"],
    "occupation": ["doctor", "scientist", "peasant", "laborer", "midwife", "immigrant", "refugee", "activist", "farmer", "nurse", "witch", "fairy", "mercenary", "robot", "alien", "mechanic", "grocery store clerk", "politician", "bureaucrat", "soldier", "prostitute", "priest", "shaman", "boxer", "smuggler", "trader", "drug dealer", "thief", "art dealer", "archaeologist", "accountant", "gang boss", "janitor", "potter", "engineer", "clerk", "servant", "poet", "artist", "musician"],
    "transitive_verb": [ "eats #object.a#", "makes #object.a#", "draws the shortest straw", "drives through #location.a# as #tragedy.a#", "drives #subject.a# insane", "plays with #object.a#", "plays with #subject.a#", "gambles and loses", "gambles and wins", "watches #subject.a#", "watches #tragedy.a#", "cooks #object.a#", "catches #subject.a#", "pushes #subject.a# down", "pushes #object.a# up a hill", "carries #subject.a# to #location.a#", "sends #subject.a# #object.a#", "receives #object.a# from #subject.a#", "cleans #location.a#", "cleans #subject.a#", "breaks #object.a#", "fixes #object.a#", "finds #subject.a# in #location.a#", "collects #object.s# and hides them in #location.a#", "destroys #subject.a#", "buys #object.a#", "sells #object.a#", "creates #object.a#", "visits #subject.a# in #location.a#", "invites #subject.a# to #location.a#"],
    "object": ["#subject#", "#thing#"],
    "thing":  ["apple", "crystal ball", "cat", "dog", "flower", "guitar", "hat", "jacket", "kite", "lemon", "notebook", "quilt", "sun", "umbrella", "violin", "watermelon", "xylophone", "butterfly", "car", "eagle", "globe", "jellyfish", "moon", "pile of #object.s#", "octopus", "piano", "queen", "robot", "sailboat", "tiger", "unicorn", "vase", "whale", "ant colony", "banana", "bottle", "egg", "honeycomb", "ice block", "jigsaw puzzle", "nail", "pepper", "rose", "sandcastle", "tulip", "violet", "arrow", "book", "chair", "eggplant", "flag", "grape", "hammer", "jackal", "mango", "sunflower"],
    "location": ["beach", "mountain", "forest", "river", "cave", "desert", "ocean", "island", "valley", "countryside", "village", "canyon", "jungle", "lake", "meadow", "volcano", "waterfall", "plateau", "wetland", "glacier", "marsh", "oasis", "prairie", "rainforest", "savanna", "tundra", "estuary", "gulch", "#noun#"],
    "tragedy": ["town burns", "bomb drops", "army descends", "flood rises", "city sinks", "comet falls"]
}


def generate_constraints() -> list:
    selector: bool = random.choice([True, False])
    perspective = "first-person" if selector else "third-person"
    
    quirks = [
        "use every letter in the alphabet at least once",
        "completely avoid a vowel of your choice",
        "don't use any commas",
        "write the entire piece as one sentence",
        "write the entire piece as a dialogue",
        "weave in something from the first random [Wikipedia](https://en.wikipedia.org/wiki/Special:Random) article you see",
        "include at least three made up slang words",
    ]
    quirk = random.choice(quirks)
    
    word_limit = f"{random.randint(1, 6) * 250} words"
    
    result = [perspective, quirk, word_limit]
    return result


def generate_prompt() -> str:
    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)
    
    story: str = grammar.flatten("#story#")
    
    constraints: list = generate_constraints()
    perspective: str = constraints[0]
    quirk: str = constraints[1]
    word_limit: str = constraints[2]
    
    result: str = f"""
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