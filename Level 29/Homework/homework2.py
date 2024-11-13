def word(text):
    words = text.split()
    return len(words)

text ="GOA is the best it school"
print("numbers of words in this text is:", word(text))