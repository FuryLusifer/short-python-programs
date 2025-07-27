from pathlib import Path

file = Path("chapter 10/alice.txt")
try:
    content = file.read_text()

except FileNotFoundError:
    print(f"Sorry the file '{file}' Does not Exist.")