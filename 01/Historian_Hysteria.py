# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Historian_Hysteria.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: xmatute- <xmatute-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/02 15:00:49 by xmatute-          #+#    #+#              #
#    Updated: 2024/12/02 15:13:48 by xmatute-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
3   4
4   3
2   5
1   3
3   9
3   3
"""
# file = "ex.txt"
file = "input.txt"

def part1():
    with open(file) as f:
        left_list = []
        right_list = []
        for line in f:
            left, right = line.split()
            left_list.append(int(left))
            right_list.append(int(right))
        ordered_left = sorted(left_list)
        ordered_right = sorted(right_list)
        print(ordered_left)
        print(ordered_right)
        distances = []
        for i in range(len(ordered_left)):
            distances.append(abs(ordered_left[i] - ordered_right[i]))
        print(distances)
        total_distance = sum(distances)
        print(total_distance)

def part2():
    with open(file) as f:
        left_list = []
        right_list = []
        for line in f:
            left, right = line.split()
            left_list.append(int(left))
            right_list.append(int(right))
        similarities = []
        for i in range(len(left_list)):
            repes = 0
            for j in range(len(right_list)):
                if left_list[i] == right_list[j]:
                    repes += 1
            similarities.append(repes * left_list[i])
        print(similarities)
        total_score = sum(similarities)
        print(total_score)
                


if __name__ == "__main__":
    part2()
    
    