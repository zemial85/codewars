def mobile_keyboard(s):
    how_many_strokes = 0
    for x in s:
        if x in lista0:
            how_many_strokes += 0
        elif x in lista1:
            how_many_strokes += 1
        elif x in lista2:
            how_many_strokes += 2
        elif x in lista3:
            how_many_strokes += 3
        elif x in lista4:
            how_many_strokes += 4
        elif x in lista5:
            how_many_strokes += 5
    print(how_many_strokes)
    return how_many_strokes


lista0 = [""]
lista1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "*", "#"]
lista2 = ["a", "d", "g", "j", "m", "p", "t", "w"]
lista3 = ["b", "e", "h", "k", "n", "q", "u", "x"]
lista4 = ["c", "f", "i", "l", "o", "r", "v", "y"]
lista5 = ["s", "z"]



