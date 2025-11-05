# Remove all of the vowels in a string (take input from user)



sentence = input("Enter a string: ")

vowel = "aeiouAEIOU"

# using list comprehension
no_vowel = ''.join([char for char in sentence if char not in vowel])
                        # or
# using decorator + comprehension
# no_vowels = ''.join(char for char in sentence if char not in vowel)

print("Sentence without vowels will be:", no_vowel)