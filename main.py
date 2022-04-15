'''Function which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side).'''

def dirReduc(arr):
    arr_copy = arr.copy()
    to_remove = [("NORTH", "SOUTH"),("EAST", "WEST"),("SOUTH","NORTH"),("WEST","EAST")]
    while True:
        x = 0
        while len(arr_copy)-1 > x:
            truple = (arr_copy[x], arr_copy[x + 1])
            if truple in to_remove:
                arr_copy[x] = 0
                arr_copy[x+1] = 0
            x += 1
        lista = []
        if not 0 in arr_copy:
            break
        for z in arr_copy:
            if z != 0:
                lista.append(z)
        arr_copy = lista

    return print(arr_copy)

dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])