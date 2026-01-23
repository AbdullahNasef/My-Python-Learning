# 1. Get the word from the user.
word = input("enter a word: ")
# 2. Define what the vowels are.
vowels_list = ['i', 'o', 'u', 'a', 'e']
# 3. Check if the word starts with one of the defined vowels.
if word[0].lower() in vowels_list:
    print(f"The {word} starts with a vowel.")
else:
    print(f"The {word} does not start with a vowel.")