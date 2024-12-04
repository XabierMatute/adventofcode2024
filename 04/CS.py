# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    CS.py                                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: xmatute- <xmatute-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/03 13:11:40 by xmatute-          #+#    #+#              #
#    Updated: 2024/12/04 12:51:15 by xmatute-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import re
"""
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

file = "ex.txt"
file = "input.txt"

XMAS = ["X", "M", "A", "S"]

matrix = open(file).readlines()
matrix = [list(line.strip()) for line in matrix]
print(matrix)
def xmascounter(x, y):
    counter = 0
    

    try:
        right = [matrix[x][y + i] for i in range(4) if y + i < len(matrix[0])]
        if right == XMAS:
            counter += 1
            print("right", right)
    except:
        pass

    try:
        left = [matrix[x][y - i] for i in range(4) if y - i >= 0]
        if left == XMAS:
            counter += 1
            print("left", left)
    except:
        pass

    try:
        up = [matrix[x + i][y] for i in range(4) if x + i < len(matrix)]
        if up == XMAS:
            counter += 1
            print("up", up)
    except:
        pass

    try:
        down = [matrix[x - i][y] for i in range(4) if x - i >= 0]
        if down == XMAS:
            counter += 1
            print("down", down)
    except:
        pass

    try:
        d1 = [matrix[x + i][y + i] for i in range(4) if x + i < len(matrix) and y + i < len(matrix[0])]
        if d1 == XMAS:
            counter += 1
            print("d1", d1)
    except:
        pass

    try:
        d2 = [matrix[x + i][y - i] for i in range(4) if x + i < len(matrix) and y - i >= 0]
        if d2 == XMAS:
            counter += 1
            print("d2", d2)
    except:
        pass

    try:
        d3 = [matrix[x - i][y + i] for i in range(4) if x - i >= 0 and y + i < len(matrix[0])]
        if d3 == XMAS:
            counter += 1
            print("d3", d3)
    except:
        pass

    try:
        d4 = [matrix[x - i][y - i] for i in range(4) if x - i >= 0 and y - i >= 0]
        if d4 == XMAS:
            counter += 1
            print("d4", d4)
    except:
        pass
    
    return counter
        



def part1():
    with open(file) as f:
        counter = 0
        x = 0
        for line in f:
            y = 0
            for c in line:
                if c == "X":
                    oldcounter = counter
                    counter += xmascounter(x, y)
                    if counter > oldcounter:
                        print(x, y)
                y += 1
            x += 1
        print(counter)

MAS = ["M", "A", "S"]

def x_mascounter(x, y):
    counter = 0
    
    if x == 0 or y == 0:
        return 0
    try:
        d1 = [matrix[x + i][y + i] for i in range(-1, 2) if x + i < len(matrix) and y + i < len(matrix[0])]
        d2 = [matrix[x + i][y - i] for i in range(-1, 2) if x + i < len(matrix) and y + i < len(matrix[0])]
        d3 = [matrix[x - i][y + i] for i in range(-1, 2) if x + i < len(matrix) and y + i < len(matrix[0])]
        d4 = [matrix[x - i][y - i] for i in range(-1, 2) if x + i < len(matrix) and y + i < len(matrix[0])]
        if (d1 == MAS):
            counter += 1
            print("d1", d1)
        if (d2 == MAS):
            counter += 1
            print("d2", d2)
        if (d3 == MAS):
            counter += 1
            print("d3", d3)
        if (d4 == MAS):
            counter += 1
            print("d4", d4)
        print(counter)
        if counter == 2:
            return 1
    except:
        pass
    
    return 0
    

def part2():
    with open(file) as f:
        counter = 0
        x = 0
        for line in f:
            y = 0
            for c in line:
                if c == "A":
                    oldcounter = counter
                    counter += x_mascounter(x, y)
                    if counter > oldcounter:
                        print(x, y)
                y += 1
            x += 1
        print(counter)

if __name__ == "__main__":
    # part1()
    part2()