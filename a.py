g = open("you_win.txt", "r")
text = g.readlines()

for line in text:
    print(line.strip())
g.close()