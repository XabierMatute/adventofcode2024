# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Red-Nosed_Reports.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: xmatute- <xmatute-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/02 15:15:57 by xmatute-          #+#    #+#              #
#    Updated: 2024/12/02 15:58:51 by xmatute-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

file = "ex.txt"
file = "input.txt"

def is_safe(report):
    increasing = True
    if report[0] == report[1]:
        return False
    if report[0] > report[1]:
        increasing = False
    for i in range(len(report) - 1):
        if increasing and report[i] >= report[i + 1]:
            return False
        if not increasing and report[i] <= report[i + 1]:
            return False
        if abs(report[i] - report[i + 1]) > 3 :
            return False 
    return True

def part1():
    with open(file) as f:
        reports = []
        for line in f:
            report = line.split()
            report = [int(x) for x in report]
            reports.append(report)
        # print(reports)
        safety = []
        for report in reports:
            safety.append(is_safe(report))
        print(safety)
        total_safe = sum(safety)
        print(total_safe)

def is_safe_leveled(report, i):
    report.pop(i)
    return is_safe(report)

def is_safe2(report):
    # increasing = True
    # if report[0] == report[1]:
    #     report.pop(1)
    #     return is_safe(report)
    # if report[0] > report[1]:
    #     increasing = False
    # for i in range(len(report) - 1):
    #     if increasing and report[i] >= report[i + 1]:
    #         report.pop(i)
    #         return is_safe(report)
    #     if not increasing and report[i] <= report[i + 1]:
    #         report.pop(i)
    #         return is_safe(report)
    #     if abs(report[i] - report[i + 1]) > 3 :
    #         report.pop(i)
    #         return is_safe(report)
    # return True
    for i in range(len(report)):
        if is_safe_leveled(report.copy(), i):
            return True
    return False

def part2():
    with open(file) as f:
        reports = []
        for line in f:
            report = line.split()
            report = [int(x) for x in report]
            reports.append(report)
        # print(reports)
        safety = []
        for report in reports:
            safety.append(is_safe2(report))
        print(safety)
        total_safe = sum(safety)
        print(total_safe)
        
if __name__ == "__main__":
    part1()
    part2()