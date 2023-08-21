"""
script that imports a json markov model and produces text from it
"""

import sys, json, random


def import_json_model(path: str) -> dict:
    with open(path) as json_file:
        model: dict = json.load(json_file)
    
    return model


def generate_text(path: str, iterations: int) -> str:
    model: dict = import_json_model(path)
    
    starter_words = [
        "you",
        "i",
        "they",
        "it",
        "these",
        "do",
        "what",
        "where",
        "why",
        random.choice(list(model.keys()))
    ]
    first_word = random.choice(starter_words)
    words = [first_word]
    for i in range(iterations):
        next_word = random.choice(model[words[i]])
        words.append(next_word)

    
    count = 0
    for index, word in enumerate(words):
        if random.randint(3, 12) <= count:
            words[index] = word + "\n"
            count = 0
        count += 1
        
        
    
    return " ".join(words)


def main():
    if len(sys.argv) < 2:
        print("Sorry, you must specify a path to a .json file")
    if sys.argv[1][-5:] != ".json":
        print("Sorry, you must specify a path to a .json file")
    
    path = sys.argv[1]
    iterations = 50 if len(sys.argv) < 3 else int(sys.argv[2])
    text_block: str = generate_text(path, iterations)
    
    print(text_block)


if __name__ == "__main__":
    main() 
