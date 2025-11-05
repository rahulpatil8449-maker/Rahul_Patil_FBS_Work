# Find all of the words in a string that are less than 5 letters (take input from user)


sentence = input("Enter a sentence: ")
less_words = [word for word in sentence.split() if(len(word) < 5)]
print("The words in the sentence having less than 5 letters are:", less_words)