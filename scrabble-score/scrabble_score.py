def score(word):
    wupper = word.upper()
    points = 0

    for i in wupper:
        if i in {"A", "E", "I", "O", "U", "L", "N", "R", "S", "T"}:
            points += 1
        elif i in {"D", "G"}:
            points += 2
        elif i in {"B", "C", "M", "P"}:
            points += 3
        elif i in {"F", "H", "V", "W", "Y"} :
            points += 4
        elif i == "K":
            points += 5
        elif i in {"J", "X"}:
            points += 8
        elif i in {"Q", "Z"}:
            points += 10
    return points
    
