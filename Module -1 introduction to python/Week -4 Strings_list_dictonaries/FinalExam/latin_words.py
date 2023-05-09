"""
Let's create a function that turns text into pig latin: a simple text transformation that modifies each word moving the first character 
to the end and appending "ay" to the end. 
For example, python ends up as ythonpay.
"""


def pig_latin(text):
    # Separate the text into words
    words = text.split()
    pig_latin_words = []
    for word in words:
        # Create the pig latin word and add it to the list
        pig_latin_word = word[1:] + word[0] + "ay"
        pig_latin_words.append(pig_latin_word)
    # Turn the list back into a phrase
    pig_latin_text = " ".join(pig_latin_words)
    return pig_latin_text


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
# Should be "rogrammingpay niay ythonpay siay unfay"
print(pig_latin("programming in python is fun"))
