

with open("sample.csv") as f:
    content = f.read()


with open("new.csv" , "w") as f:
    f.write(content)