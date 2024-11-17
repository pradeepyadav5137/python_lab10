
with open("05.txt") as f:
    content = f.readlines()

file = " ".join(line.strip() for line in content)

print(file)