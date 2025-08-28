alpha = input("Enter an alphabet: ")

if(alpha in 'aeiouAEIOU'):     #"in" operator is used which is including all the vowels in that variable(alpha) and excluding all other alphabets(consonants)
    print("The given alphabet is a vowel.")
else:
    print("The given alphabet is a consonant.")