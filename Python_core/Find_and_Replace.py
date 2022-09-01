import re
str="Python is a high-level, interpreted, general-purpose programming code."
changeWord="code"
new=re.sub(changeWord,"language",str)
print(new)