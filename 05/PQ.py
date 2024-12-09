# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    PQ.py                                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: xmatute- <xmatute-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/05 11:18:04 by xmatute-          #+#    #+#              #
#    Updated: 2024/12/05 11:44:02 by xmatute-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

file = "ex.txt"
file = "input.txt"

def is_valid(l, rules):
    i = 0
    for n in l:
        for r in rules:
            if n == r[0]:
                for pn in l[0:i]:
                    if pn == r[1]:
                        return False
        i += 1
    return True

def part1():
    with open(file) as f:
        data = f.read().splitlines()
        rules = [list(map(int, line.split("|"))) for line in data if line.find("|") != -1]
        print(rules)
        lists = [list(map(int, line.split(","))) for line in data if line.find(",") != -1]
        print(lists)
        valid_lists = []
        for l in lists:
            if is_valid(l, rules):
                valid_lists.append(l)
        print(valid_lists)
        middle_numbers = []
        for l in valid_lists:
            middle_numbers.append(l[len(l) // 2])
        print(middle_numbers)
        result = sum(middle_numbers)
        print(result)

def fix(l, rules):
    i = 0
    for n in l:
        for r in rules:
            if n == r[0]:
                j = 0
                for pn in l[0:i]:
                    if pn == r[1]:
                        tmp = l[i]
                        l[i] = pn
                        l[j] = tmp
                    j += 1     
        i += 1
    if not is_valid(l, rules):
        return fix(l, rules)
    return l

def part2():
    with open(file) as f:
        data = f.read().splitlines()
        rules = [list(map(int, line.split("|"))) for line in data if line.find("|") != -1]
        print(rules)
        lists = [list(map(int, line.split(","))) for line in data if line.find(",") != -1]
        print(lists)
        valid_lists = []  #tecnically invalid lists
        for l in lists:
            if not is_valid(l, rules):
                valid_lists.append(l)
        for l in valid_lists:
            l = fix(l, rules)
        print(valid_lists)
        middle_numbers = []
        for l in valid_lists:
            middle_numbers.append(l[len(l) // 2])
        print(middle_numbers)
        result = sum(middle_numbers)
        print(result)


if __name__ == "__main__":
    # part1()
    part2()