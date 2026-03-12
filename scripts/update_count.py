import os
import re

easy = 0
medium = 0
hard = 0

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".cpp"):
            path = root.lower()

            if "easy" in path:
                easy += 1
            elif "medium" in path:
                medium += 1
            elif "hard" in path:
                hard += 1

total = easy + medium + hard

with open("README.md", "r") as f:
    content = f.read()

content = re.sub(r'<!--EASY-->.*?<!--EASY-->', f'<!--EASY-->{easy}<!--EASY-->', content)
content = re.sub(r'<!--MEDIUM-->.*?<!--MEDIUM-->', f'<!--MEDIUM-->{medium}<!--MEDIUM-->', content)
content = re.sub(r'<!--HARD-->.*?<!--HARD-->', f'<!--HARD-->{hard}<!--HARD-->', content)
content = re.sub(r'<!--TOTAL-->.*?<!--TOTAL-->', f'<!--TOTAL-->{total}<!--TOTAL-->', content)

with open("README.md", "w") as f:
    f.write(content)
