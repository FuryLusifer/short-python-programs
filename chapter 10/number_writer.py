from pathlib import Path
import json

numbers = [25,78,41,89,63]
file = Path("chapter 10/numbers.json")
content = json.dumps(numbers)
print(content)
file.write_text(content)