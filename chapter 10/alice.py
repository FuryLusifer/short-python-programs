from pathlib import Path

file = Path("chapter 10/alice.txt")
try:
    content = file.read_text(encoding='utf-8')

except FileNotFoundError:
    print(f"Sorry the file '{file}' Does not Exist.")

else:
    # counting the approximate numeber of words in the book.
    words = content.split()
    total_words = len(words)
    print(f"The Book '{file.name}' has about {total_words:,} words.")