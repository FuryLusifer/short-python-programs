from pathlib import Path

file = Path("chapter 10/pi_digits.txt")
content = file.read_text()

for line in content.splitlines():
    print(line)