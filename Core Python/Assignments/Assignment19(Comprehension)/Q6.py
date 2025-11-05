# Use a dictionary comprehension to count the length of each word in a sentence (take input from user)


sentence = input("Enter the sentence: ")
count_length = {word: len(word) for word in sentence.split()}
print("The count of each word in the Sentence is:", count_length)