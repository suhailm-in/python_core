import  re
pattern="python"

if re.match(pattern,"pythonworld hello whoami"):
    print("matched")
else:
    print("not mached")