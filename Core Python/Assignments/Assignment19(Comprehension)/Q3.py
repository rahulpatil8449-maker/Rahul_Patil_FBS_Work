# Count the number of spaces in a string (take input from user)


sentence = input("Enter any Sentence: ")
print(sentence)
space = sum([1 for i in sentence if i == ' '])        # this
                # or
# space = sum(1 for i in sentence if i == ' ')      or this no need of using list
print(space)