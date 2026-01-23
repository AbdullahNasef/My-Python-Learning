word = input("Enter a word:")
print('-' * 20)
lst_word = list(word)

lst_word.reverse()

reversed_word = ''.join(lst_word)
print("Reversed word is:", reversed_word)