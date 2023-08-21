"""
A script for generating flash fiction prompts from tracery grammars
"""

import tracery, random
from tracery.modifiers import base_english


rules = {
    "story": [
        "#subject.a# #transitive_verb#",
    ],
    "subject": ["#person#", "#occupation#", "#person#", "#occupation#", "#person#", "#occupation#", "group of #people#", "group of #occupation.s#"],
    "person": ["teenager", "kid", "boy", "girl", "#age# man", "#age# woman"],
    "age": ["young", "old", "middle-aged"],
    "occupation": ["doctor", "scientist", "peasant", "laborer", "midwife", "immigrant", "refugee", "activist", "farmer", "nurse", "witch", "fairy", "mercenary", "robot", "alien", "mechanic", "grocery store clerk", "politician", "bureaucrat", "soldier", "prostitute", "priest", "shaman", "boxer", "smuggler", "merchant", "drug dealer", "thief", "art dealer", "archaeologist", "accountant", "gang boss", "janitor", "potter", "engineer", "clerk", "servant", "poet", "artist", "musician"],
    "people": ["teenagers", "kids", "boys", "girls", "men", "women", "old men", "old women"],
    "transitive_verb": [ "eats #object.a#", "makes #thing.a#", "draws the shortest straw", "drives through #location.a# and #tragedy.a#", "drives #subject.a# insane", "plays with #object.a#", "plays with #subject.a#", "gambles and loses", "gambles and wins", "watches #subject.a#", "watches #tragedy.a#", "cooks #object.a#", "catches #subject.a#", "pushes #subject.a# #pushed_into#", "pushes #object.a# up a hill", "transports #object.a# to #location.a#", "sends #subject.a# #object.a#", "receives #object.a# from #subject.a#", "cleans #location.a#", "cleans #subject.a#", "breaks #object.a#", "fixes #thing.a#", "helps #subject.a#", "finds #subject.a# in #location.a#", "collects #object.s# and hides them in #location.a#", "destroys #subject.a#", "buys #object.a#", "sells #object.a#", "hunts for #object.a#", "kills #subject.a#", "argues with #object.a#", "visits #subject.a# in #location.a#", "invites #subject.a# to #location.a#"],
    "object": ["#subject#", "#thing#"],
    "thing":  ["apple", "crystal ball", "cat", "dog", "flower", "guitar", "hat", "jacket", "kite", "lemon", "notebook", "quilt", "sun", "umbrella", "violin", "watermelon", "xylophone", "butterfly", "car", "eagle", "globe", "jellyfish", "moon", "pile of #things.s#", "octopus", "piano", "queen", "robot", "sailboat", "tiger", "unicorn", "vase", "whale", "ant colony", "banana", "bottle", "egg", "honeycomb", "ice block", "jigsaw puzzle", "nail", "pepper", "rose", "sandcastle", "tulip", "violet", "arrow", "book", "chair", "eggplant", "flag", "grape", "hammer", "jackal", "mango", "sunflower"],
    "location": ["beach", "mountain", "forest", "river", "cave", "desert", "ocean", "island", "valley", "countryside", "village", "canyon", "jungle", "lake", "meadow", "volcano", "waterfall", "plateau", "wetland", "glacier", "marsh", "oasis", "prairie", "rainforest", "savanna", "tundra", "estuary", "gulch"],
    "tragedy": ["town burn", "bomb drop", "army descend", "flood rise", "city sink", "comet fall"],
    "pushed_into": ["to the ground", "down a flight of stairs", "into the ocean", "into a cliff", "into a well", "into a cave", "into #subject.a#", "into the line of fire", "into a basement"]
}


def generate_fiction_exercise() -> str:
    perspectives = ["first", "third", "third"]
    perspective = random.choice(perspectives) + "-person"

    word_limit = f"{random.randint(1, 6) * 250} words"

    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)
    
    story: str = grammar.flatten("#story#")
    
    result: str = f"""
    STORY: {story}
    PERSPECTIVE: {perspective}
    WORD LIMIT: {word_limit}
    
    Good luck!
    """
    return result


def main():
    prompt: str = generate_fiction_exercise()
    print(prompt)


if __name__ == "__main__":
    main()