from pathlib import Path

path = Path('chapter 10/pi_digits.txt')
content = path.read_text()
print(content)

lines = content.splitlines()
for line in lines:
    print(line)
