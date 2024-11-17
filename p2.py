c_keywords = [
    "auto", "break", "case", "char", "const", "continue", "default", "do", "double", 
    "else", "enum", "extern", "float", "for", "goto", "if", "int", "long", "register", 
    "return", "short", "signed", "sizeof", "static", "struct", "switch", "typedef", 
    "union", "unsigned", "void", "volatile", "while"
]

def count_keywords_in_c_file(file_path):
    
    keyword_counts = {key: 0 for key in c_keywords}

    with open(file_path, 'r') as file:
        content = file.read() 

    
    for keyword in c_keywords:
        keyword_counts[keyword] = content.count(keyword)

    
    keyword_counts = {key: count for key, count in keyword_counts.items() if count > 0}

    return keyword_counts

def main():
    filepath = input("Enter the file path : ")
    content = count_keywords_in_c_file(filepath)

    with open("key_word.csv", "w") as f:
        f.write("Keyword,Count\n") 
        for keyword, count in content.items():
            f.write(f"{keyword},{count}\n")

main()