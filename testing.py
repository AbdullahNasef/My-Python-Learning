nested_list = [
    ["Hello", "from", "Codezilla"],
["Python", "Course", "is", "awesome"],
["I", "enjoy", "learning", "Python", "with", "Codezilla"]
]
words = []
for lst in nested_list:
    for word in lst:
        words.append(word)

print(words)