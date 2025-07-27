from pathlib import Path

file = Path("chapter 10/pi_million_digits.txt")
content = file.read_text()
lines = content.splitlines()

pi_string = ""

for line in lines:
    pi_string += line.strip()
    
print(f"Pi string upto 52 digits:\n{pi_string[:52]}")
print(len(pi_string))