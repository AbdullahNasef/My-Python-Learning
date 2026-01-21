nested_list = [["Hello", "from", "Codezilla"],
["Python", "Course", "is", "awesome"],
["I", "enjoy", "learning", "Python", "with", "Codezilla"]]
flat_lst = []
for lst in nested_list:
    flat_lst.extend(lst)
print(flat_lst)
