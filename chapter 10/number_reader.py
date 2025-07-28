from pathlib import Path
import json

file = Path("chapter 10/numbers.json")
contents = file.read_text()
numbers = json.loads(contents)
print(numbers)