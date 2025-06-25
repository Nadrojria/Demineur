print("****Demineur****")

def grill(size, bomb):
    array_grill = [] #array including array_line
    for i in range(size):
        array_line = []
        for f in range(size):
            array_line.append(0)
        array_grill.append(array_line)
        print(array_line)

grill(5, 4)


