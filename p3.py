
newword =[]
with open("03.txt") as f:
    content = f.read()
    words = content.split()

for word in words:
    if word not in newword:
        newword.append(word)

print(sorted(newword))
