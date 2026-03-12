import os
import re

total = 0

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".cpp"):
            total += 1

with open("README.md", "r") as f:
    content = f.read()

content = re.sub(r'<!--TOTAL-->.*?<!--TOTAL-->', f'<!--TOTAL-->{total}<!--TOTAL-->', content)

with open("README.md", "w") as f:
    f.write(content)
