from pathlib import Path

def count_occurence(query):
    file = Path("chapter 10/alice.txt")
    try:
        content = file.read_text(encoding='utf-8').lower()

    except FileNotFoundError:
        print(f"The file {file.name} could not be found.")
        return 0

    else:
        return content.count(query.lower())

query = input("Enter the word you want to count: ")
print(f"Total Occurence of '{query}' in the file: {count_occurence(query)}")