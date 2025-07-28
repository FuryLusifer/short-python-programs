from pathlib import Path
import json

file = Path("chapter 10/favorite numbers.json")
try:
    content = file.read_text()

except FileNotFoundError:
    print(f"The file {file.name} could not be located.")

else:
    fav_num = json.loads(content)
    print(f"Your favorite number: {fav_num}")