# Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary

                #### CHATGPT
# # Take input string from user
# text = input("Enter a string: ")

# # Step 1: Convert the string into words manually
# words = []
# word = ""

# for ch in text + " ":       # Add space at end to capture last word
#     if ch != " ":           # If character is not space → add to current word
#         word += ch
#     else:
#         if word != "":      # If we found a word, add it to the list
#             words.append(word)
#             word = ""       # Reset for next word

# # Step 2: Create empty dictionary for word frequency
# freq = {}

# # Step 3: Count words manually
# for w in words:
#     found = False
#     for key in freq:
#         if key == w:
#             freq[key] += 1
#             found = True
#             break
#     if not found:
#         freq[w] = 1

# # Step 4: Display result
# print("Word Frequency:")
# for k in freq:
#     print(k, ":", freq[k])




str = input("Enter a string: ")

words = str.split()     # spliting the string(str) into separate words

freq = {}       # accepting empty dictionary

for word in words:      # counting the frequency of words manually
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("Frequency of words: ")
for word in freq:
    print(word, ":", freq[word])