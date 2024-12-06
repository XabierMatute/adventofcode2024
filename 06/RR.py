# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    RR.py                                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: xmatute- <xmatute-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/05 11:18:04 by xmatute-          #+#    #+#              #
#    Updated: 2024/12/06 20:31:39 by xmatute-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

file = "ex.txt"
file = "input.txt"

matrix = open(file).readlines()
matrix = [list(line.strip()) for line in matrix]
direction = 0
import sys

sys. setrecursionlimit(42424242)

def in_limits(x, y):
    return x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0])

def patrol(x, y):
    for line in matrix:
        print("".join(line))
    counter = 0
    for line in matrix:
        counter += line.count("X")
    print(counter)

    global direction
    new_x = x
    new_y = y

    matrix[new_x][new_y] = "X"
    #usando el modulo para saber la direccion
    if direction % 4 == 0:
        new_x -= 1
    elif direction % 4 == 1:
        new_y -= 1
    elif direction % 4 == 2:
        new_x += 1
    elif direction % 4 == 3:
        new_y += 1
    if in_limits(new_x, new_y) and matrix[new_x][new_y] != "#":
        patrol(new_x, new_y)
    if in_limits(new_x, new_y) and matrix[new_x][new_y] == "#":
        direction -= 1
        patrol(x, y)
    
        
    

def part1():
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "^":
                matrix[i][j] = "X"
                patrol(i, j)
                break
    for line in matrix:
        print("".join(line))
    counter = 0
    for line in matrix:
        counter += line.count("X")
    print(counter)


def part2():
    pass

if __name__ == "__main__":
    part1()
    # part2()