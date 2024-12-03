# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    MIO.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: xmatute- <xmatute-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/03 13:11:40 by xmatute-          #+#    #+#              #
#    Updated: 2024/12/03 13:45:14 by xmatute-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import re
"""
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""

""""
mul(X,Y)
"""

file = "ex.txt"
file = "input.txt"


def part1():
    with open(file) as f:
        text = f.read()
        pattern = r'mul\(\d{1,3},\d{1,3}\)'
        matches = re.findall(pattern, text)

        print(matches)
        mults = []
        for match in matches:
            print(match)
            x = int(match[4:match.index(",")])
            y = int(match[match.index(",") + 1:-1])
            print(x, y)
            print(x * y)
            mults.append(x * y)
        print(mults)
        total = sum(mults)
        print(total)
        

def part1logic(text):
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    matches = re.findall(pattern, text)

    print(matches)
    mults = []
    for match in matches:
        print(match)
        x = int(match[4:match.index(",")])
        y = int(match[match.index(",") + 1:-1])
        print(x, y)
        print(x * y)
        mults.append(x * y)
    print(mults)
    total = sum(mults)
    print(total)
    

def part2():
    # file = "ex2.txt"

    with open(file) as f:
        text = f.read()
        dos_pos = [m.start() for m in re.finditer('do\(\)', text)]
        donts_pos = [m.start() for m in re.finditer('don\'t\(\)', text)]
        print(dos_pos)
        print(donts_pos)

        text_list = list(text)
        delete = False
        for i in range(len(text)):
            if i in dos_pos:
                delete = False
            if i in donts_pos:
                delete = True
            if delete:
                text_list[i] = ""
        text = "".join(text_list)
        print(text)
        part1logic(text)

        
        

    

if __name__ == "__main__":
    # part1()
    part2()