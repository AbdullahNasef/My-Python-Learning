# A long piece of text
Text = """
Python has a set of built-in methods that you can use on strings. 
Note: All string methods returns new values. They do not change
 the original string
"""

list_of_word = Text.split()
print(list_of_word)
num_of_word = len(list_of_word)
print(f'Number of words: {num_of_word}')