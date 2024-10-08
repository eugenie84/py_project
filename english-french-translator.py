
'''Python program
student name: Eugenie Tsafack
date: 10/4/2024
file name: english-french-translator.py

Instructions: Create an english to french translator program.
- The program takes a word from the user as an input and translates it using a dictionary data type as a vocabulary
- Please add the translation of "prune" in your dictionary
- If a word is not in the code vocabulary, print ([word] is not in my memory)
'''
# create a dictionary that will translate a english word to a french word
english_french = {
    "prune": "élaguer",
    "school": "école",
    "impermeable": "imperméable",
    "apple": "pomme",
    "book":  "livre",
    "car": "voiture",
    "dog":  "chien",
    "cat":  "chat",
    "house":  "maison",
    "water":  "eau",
    "sun": "soleil",
    "tree": "arbre",
    "flower": "fleur",
    "food":  "nourriture",
    "friend": "ami",
    "love": "amour",
    "bird": "oiseau",
    "street": "rue",
    "city":  "ville",
    "door":  "porte",
    "window":  "fenêtre",
    "music":  "musique",
    "phone":  "téléphone",
    "table": "table",
    "chair":  "chaise",
    "bread": "pain",
    "milk":  "lait",
    "fish": "poisson",
    "shoe": "chaussure",
    "clothes":  "vêtements",
    "pen": "stylo",
    "mountain": "montagne",
    "river": "rivière",
    "forest":  "forêt",
    "beach": "plage",
    "bicycle": "vélo",
    "train": "train",
    "airplane": "avion",
    "family":  "famille",
    "work": "travail",
    "happiness": "bonheur",
    "mermaid": "sirène",
        
    }

# create a dictionary that will translate a french word to a english word
french_english = {
    "élaguer": "prune",
    "école": "school",
    "imperméable": "impermeable",
    "pomme": "apple",
    "livre": "book",
    "voiture": "car",
    "chien": "dog",
    "chat": "cat",
    "maison": "house",
    "eau": "water",
    "soleil": "sun",
    "arbre": "tree",
    "fleur": "flower",
    "nourriture": "food",
    "ami": "friend",
    "amour": "love",
    "oiseau": "bird",
    "rue": "street",
    "ville": "city",
    "porte": "door",
    "fenêtre": "window",
    "musique": "music",
    "téléphone": "phone",
    "table": "table",
    "chaise": "chair",
    "pain": "bread",
    "lait": "milk",
    "poisson": "fish",
    "chaussure": "shoe",
    "vêtements": "clothes",
    "stylo": "pen",
    "montagne": "mountain",
    "rivière": "river",
    "forêt": "forest",
    "plage": "beach",
    "vélo": "bicycle",
    "train": "train",
    "avion": "airplane",
    "famille": "family",
    "travail": "work",
    "bonheur": "happiness",
    "sirène": "mermaid",
    "prune": "plum"
    
}

# asking the user to choose the language he/ she wants to use
language = input("Please choose a language you want to use between English and French\t").lower()

# set a condition to get the word in a dictionary
word= input("Please enter a word you want to translate \t").lower()
word_translate1 = english_french.get(word)
word_translate2 = french_english.get(word)

# check whether the word and a language are in a dictionary or not
if language == "english":
    
    if word_translate1 :
        print(f"{word.capitalize()} in french is: {word_translate1}")
    
    else:
        print(f"{word.capitalize()} is not in my memory!")
    
elif language == "french":
    
    if word_translate2 :
        print(f"{word.capitalize()} in english is: {word_translate2}")
    
    else:
        print(f"{word.capitalize()} is not in my memory!")
else:
    print("Sorry! This language does not exist in my memory")


    

