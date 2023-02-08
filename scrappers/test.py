

text = ""

with open(f"txt/temp.txt" , "r") as f: #read&write
    for line in f:
        if(line.strip()):
            text += line

print(text)
