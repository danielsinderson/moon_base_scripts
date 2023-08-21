"""
script to import a text file,
create a markov model of it, 
and export that model to JSON for future use 
"""

import sys, string, json


def import_and_clean_text(path: str) -> str:
    with open(path) as text_file:
        text = text_file.read()
        
    text = text.replace("-", " ")
    cleaned_text = ""
    for char in text:
        if char in string.punctuation:
            continue
        if char in string.digits:
            continue    
        cleaned_text += char
    
    cleaned_text = cleaned_text.lower()
    cleaned_text = cleaned_text.replace("\n", " ")
    cleaned_text = cleaned_text.encode("ascii", "ignore")
    cleaned_text = cleaned_text.decode()
    
    return cleaned_text


def create_markov_model(text: str) -> dict:
    model = {}
    words = text.split()
    for index, word in enumerate(words[:-2]):
        if word in model:
            model[word].append(words[index + 1])
        else:
            model[word] = [words[index + 1]]
    
    return model
    #return optimize_model(model)


def export_model_to_json(model: dict, path: str):
    new_path = path[:-3] + "json"
    print(new_path)
    with open(new_path, "w") as json_file:
        json.dump(model, json_file, indent=2)


def create_model(path: str):
    text: str = import_and_clean_text(path)
    model: dict = create_markov_model(text)
    export_model_to_json(model, path)


def main():
    if len(sys.argv) < 2:
        print("Sorry, you must specify a path to a .txt file")
    if sys.argv[1][-4:] != ".txt":
        print("Sorry, you must specify a path to a .txt file")
    
    path = sys.argv[1]
    create_model(path)


if __name__ == "__main__":
    main() 