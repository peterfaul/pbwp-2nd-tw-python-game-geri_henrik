import string

dictionary = {"a": ["0"] * 10,
     "b": ["0"] * 10,
     "c": ["0"] * 10,
     "d": ["0"] * 10,
     "e": ["0"] * 10,
     "f": ["0"] * 10,
     "g": ["0"] * 10,
     "h": ["0"] * 10,
     "i": ["0"] * 10,
     "j": ["0"] * 10}

letters = list(string.ascii_lowercase[:10])
#print(d.get("a")[2])
# Horizontal ship placement
for i in range(5):
    dictionary["b"][i+1] = "5"
for k, v in sorted(dictionary.items()):
     print(k,v)

#vertical ship placement
for i in letters[4:9]:
    dictionary[i][1] = "5"
for k, v in sorted(dictionary.items()):
     print(k,v)
