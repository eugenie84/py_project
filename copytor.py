'''Python program
student name: Eugenie Tsafack
date: 10/24/2024
file name: copytor.py
Instructions: Write a function called copy, which takes in a file name and a new file name and copies the contents of the first file into the second file.

'''

import shutil

# define a copy function


def copy_file():
    
    with open("story.txt", "w") as file:
        file.write("Alice finding tiny door behind curtain\n")
        file.write("Alice opened the door and found that it led into a small passage, not much larger than a rat-hole: she knelt down and looked along the passage into the loveliest garden you ever saw. How she longed to get out of that dark hall, and wander about among those beds of bright flowers and those cool fountains, but she could not even get her head though the doorway; `and even if my head would go through,' thought poor Alice, `it would be of very little use without my shoulders. Oh, how I wish I could shut up like a telescope! I think I could, if I only know how to begin.' For, you see, so many out-of-the-way things had happened lately, that Alice had begun to think that very few things indeed were really impossible.\n")
        file.write("There seemed to be no use in waiting by the little door, so she went back to the table, half hoping she might find another key on it, or at any rate a book of rules for shutting people up like telescopes: this time she found a little bottle on it, (`which certainly was not here before,' said Alice,) and round the neck of the bottle was a paper label, with the words `DRINK ME' beautifully printed on it in large letters.")
        print("Original file written:", file.name)
        

    # copy the text into a new file
    shutil.copy("story.txt", "story_copy.txt")
    print ("File copied to:", "story_copy.txt")
        
# calling a copy function
copy_file()
