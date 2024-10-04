
'''Python program
student name: Eugenie Tsafack
date: 10/4/2024
file name: english-french-translator.py

Instructions: Create an english to french translator program.
- The program takes a word from the user as an input and translates it using a dictionary data type as a vocabulary
- Please add the translation of "prune" in your dictionary
- If a word is not in the code vocabulary, print ([word] is not in my memory)
'''
# create a dictionary that will translate a english word to french
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

# set a condition to get the word in a dictionary
word= input("Please enter a word you want to translate \t")
word_translate = english_french.get(word)

# check whether the word is in a dictionary or not
if word_translate :
    print(f"{word} in french is: {word_translate}")
    
    
else:
    print(f"{word} is not in my memory!")
    

