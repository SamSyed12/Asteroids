
scores = {}
highscore_file = open("scores.txt", "r")
for line in highscore_file:
    line_list = []
    line_list = line.split()
    g = line_list[0]
    y = int(line_list[1])
    if g in scores:
        if scores [g] < y:
            scores [g] = y
    else:
        scores [g] = y


while True:
    name = input("Enter a name:").lower()
    if name == "quit":
        break
    if name in scores:
        print(scores[name])
    else:
        print( "No score found for " + name)













