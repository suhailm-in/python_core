import re

pattern="[A-Z][0-9][a-z]"
if re.search(pattern,"S7t"):
    print("correct")
else:
    print("not correct")