import pickle

notes = []

# TODO: Using the pickle module...

# A. If notes.pickle exists, read it in using pickle and assign the content to
#   the notes variable

try:
	contents = pickle.load(open("notes.pickle", "rb"))
	print(contents)
	notes.extend(contents)

except FileNotFoundError:
	pass

# B. Print out notes

print(notes)

# C. Read in a string from the user using input() and append it to notes
print("input:")
new_content = input()
notes.append(new_content)
print(notes)

# D. Save notes to notes.pickle
pickle.dump(notes, open("notes.pickle","wb"))

