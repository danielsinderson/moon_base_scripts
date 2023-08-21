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


nouns =  ["dog", "tree", "car", "book", "chair", "table", "house", "phone", "ball", "cup", "cat", "bike", "bed", "shoe", "hat", "sun", "moon", "key", "door", "window", "river", "mountain", "ocean", "cloud", "bird", "fish", "flower", "bridge", "road", "computer", "pen", "pencil", "wallet", "clock", "mirror", "guitar", "umbrella", "brush", "toothbrush", "lamp", "lampshade", "candle", "mirror", "painting", "camera", "microphone", "wallet", "hat", "umbrella", "sunglasses", "globe", "glasses", "bookshelf", "vase", "chair", "pillow", "blanket", "coffeemaker", "couch", "scarf", "camera", "passport", "dictionary", "newspaper", "notebook", "bottle", "plate", "fork", "spoon", "knife", "napkin", "tablecloth", "watch", "bracelet", "necklace", "ring", "earrings", "puzzle", "painting", "sketch", "sculpture", "laptop", "desktop", "tablet", "mouse", "keyboard", "monitor", "galaxy", "nebula", "quasar", "supernova", "comet", "asteroid", "planet", "constellation", "telescope", "observatory", "eclipse", "parallax", "orbit", "cosmos", "molecule", "cell", "genome", "species", "ecosystem", "biodiversity", "ecology", "mutation", "chlorophyll", "mitosis", "meiosis", "enzymes", "chloroplast", "artifact", "excavation", "ancestor", "ritual", "kinship", "mythology", "ethnography", "nomad", "agriculture", "settlement", "burial", "shaman", "hypothesis", "fossil", "radiocarbon", "ceramics", "hominid", "evolution", "ethnology", "kinship", "human", "archaeology", "excavation", "heritage", "primate", "mitochondria", "language", "gene", "behavior", "nature", "culture", "adaptation", "astronomy", "taxonomy", "chimpanzee", "migration", "monolith", "pottery", "language", "homology", "stratigraphy"]
adjectives = ['happy', 'red', 'big', 'shiny', 'tall', 'brave', 'kind', 'loud', 'soft', 'sweet', 'angry', 'sunny', 'calm', 'funny', 'smart', 'quick', 'thick', 'thin', 'rich', 'poor', 'warm', 'cold', 'busy', 'lazy', 'proud', 'quiet', 'dark', 'bright', 'light', 'heavy', 'young', 'old', 'fast', 'slow', 'fresh', 'stale', 'tiny', 'huge', 'bitter', 'sour', 'spicy', 'mild', 'smooth', 'rough', 'fierce', 'gentle', 'famous', 'ordinary', 'unique', 'elegant', 'clumsy', 'curious', 'serious', 'playful', 'crazy', 'silly', 'wild', 'mellow', 'dull', 'vivid', 'daring', 'timid', 'cheerful', 'gloomy', 'peaceful', 'vibrant', 'dazzling', 'mysterious', 'transparent', 'fragile', 'robust', 'glorious', 'graceful', 'harmonious', 'lively', 'precious', 'rigorous', 'spontaneous', 'tranquil', 'versatile', 'zesty', 'adorable', 'bouncy', 'charming', 'delightful', 'exuberant', 'fascinating', 'genuine', 'inspiring', 'jovial', 'kooky', 'lovable', 'melodic', 'nostalgic', 'optimistic', 'pensive', 'quirky', 'radiant', 'sincere', 'tender']
verbs = ['run', 'eat', 'jump', 'sleep', 'swim', 'write', 'read', 'sing', 'dance', 'play', 'work', 'study', 'drive', 'talk', 'listen', 'watch', 'climb', 'paint', 'cook', 'draw', 'fly', 'skip', 'laugh', 'cry', 'smile', 'think', 'bake', 'code', 'surf', 'hike', 'ride', 'travel', 'explore', 'photograph', 'meditate', 'design', 'compute', 'calculate', 'build', 'invent', 'compose', 'assemble', 'balance', 'equip', 'hammer', 'navigate', 'operate', 'paddle', 'plant', 'race', 'repair', 'sculpt', 'spin', 'train', 'unite', 'vary', 'weave', 'zoom', 'adapt', 'broadcast', 'capture', 'deliver', 'endure', 'foster', 'gather', 'hatch', 'illuminate', 'jog', 'knead', 'leap', 'mold', 'navigate', 'observe', 'perform', 'quicken', 'radiate', 'sprint', 'transform', 'understand', 'vacuum', 'wander', 'x-ray', 'yield', 'zap']


def fill_word_list(words: list, count: int):
    word_list = []
    for i in range(count):
        word = random.choice(words)
        while word in word_list:
            word = random.choice(words)
        word_list.append(word)
    return word_list


def generate_word_lists() -> dict:
    word_lists = {
        "nouns": fill_word_list(nouns, 10),
        "adjectives": fill_word_list(adjectives, 10),
        "verbs": fill_word_list(verbs, 10)
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
    max_end_stops = random.randint(2, int(structure["total_lines"] / 2) + 1)
    end_stop_constraint = f"no more than {max_end_stops} end stops."
    return end_stop_constraint


def generate_quirk() -> str:
    quirks = [
        "must have an epigraph you've made up yourself.",
        "must follow a consistent meter.",
        "must be an acrostic.",
        "must use only two kinds of punctuation max.",
        "must not use a vowel of your choice.",
        "must only use 10 consonants.",
        "must use every consonant at least once.",
        "must have a consistent syllable count for every line."
    ]
    quirk = random.choice(quirks)
    return quirk


def format_prompt(word_lists: dict,
                  structure: dict,
                  sonic_constraint: str,
                  end_stop_constraint: str,
                  quirk: str
                  ) -> str:
    formatted_prompt = f"""
    Your poem must adhere to the following constraints:
    1. It must contain {structure['stanzas']} stanzas.
    2. There must be {structure['lines_per_stanza']} lines per stanza.
    3. It must have {sonic_constraint}
    4. It must contain {end_stop_constraint}
    5. It must contain a noun, an adjective, and a verb from the following lists for every stanza
    6. As an added, optional challenge, it {quirk}\n
    Nouns: {word_lists["nouns"]}
    Adjectives: {word_lists["adjectives"]}
    Verbs: {word_lists["verbs"]}\n
    Good luck!
    """
    return formatted_prompt


def generate_poetry_exercise() -> str:
    word_lists: dict = generate_word_lists()
    structure: dict = generate_structure()
    sonic_constraint: str = generate_sonic_constraint()
    end_stop_constraint: str = generate_end_stop_constraint(structure=structure)
    quirk = generate_quirk()
    
    prompt = format_prompt(word_lists=word_lists,
                           structure=structure,
                           sonic_constraint=sonic_constraint,
                           end_stop_constraint=end_stop_constraint,
                           quirk=quirk
                           )
    return prompt


def main():
    prompt: str = generate_poetry_exercise()
    print(prompt)


if __name__ == "__main__":
    main()