
vowels = ["a" , "e", "i" , "o" ,  "u"]
vowel_count = 0
const_count = 0


with open("04.txt") as f:
    content = f.read()


for c in content:
    if c.lower() in vowels:
        vowel_count +=1
    elif c.isalpha():
        const_count += 1

print(len(content))
print(vowel_count)
print(const_count)