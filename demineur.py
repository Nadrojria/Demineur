import random

print("****Demineur****")

bomb = " X "
empty = " - "
no_bomb = " 0 "
array_grid = []


#### PRINCIPAL FUNCTION ####
############################

def grid(lenght, width, number):
    for row in range(lenght):
        array_line = []
        for column in range(width):
            array_line.append(empty)
        array_grid.append(array_line)

    bombs(lenght, width, number)
    show_grid(array_grid)
    tries_win_or_loose(lenght, width, number)


#### SECONDARY FUNCTION ####
############################

def bombs(lenght, width, number):
    count = 0
    while count < number:
        random_lenght = random.randint(0, lenght-1)
        random_width = random.randint(0, width-1)
        if array_grid[random_lenght][random_width] == empty: 
            array_grid[random_lenght][random_width] = bomb
            count += 1


def tries_win_or_loose(lenght, width, number):
    tries = 0
    while tries < ((lenght*width)-number):
        result = user_choice()

        if result == True:
            print("GAME OVER")
            show_grid_solution(array_grid)
            exit()

        if tries == ((lenght*width)-number)-1:
            print("YOU WIN")
            show_grid_solution(array_grid)
            exit()

        show_grid(array_grid)
        tries +=1


def show_grid(grid):
    for row in grid:
        line = ""
        for elem in row:
            if elem == bomb:
                elem = empty
            line += elem
        print(line)


def show_grid_solution(grid):
    for row in grid:
        line = ""
        for elem in row:
            line += elem
        print(line)


def user_choice():
    user_row = input("Enter a row: ")
    user_column = input("Enter a column: ")

    if array_grid[int(user_row)][int(user_column)] == bomb: 
        return True
      
    if array_grid[int(user_row)][int(user_column)] == empty: 
        array_grid[int(user_row)][int(user_column)] = no_bomb
        return False


#### RUN THE CODE ####
######################

grid(2, 2, 1)



