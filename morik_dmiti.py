from random import *
from math import sqrt

field = [[2, -3], [-1, 2]]
amountA = 0
amountB = 0
count_games = 100

with open("resultA.txt", "w", encoding="utf-8") as file1:
    with open("resultB.txt", "w", encoding="utf-8") as file2:
        for i in range(count_games):
            choiceA_line = randint(0, 1)
            choiceB_line = randint(0, 1)
            choiceA_column = randint(0, 1)
            choiceB_column = randint(0, 1)

            amountA += field[choiceA_line][choiceA_column]
            amountB += field[choiceB_line][choiceB_column]
            file1.write(f"Выбор А: [{choiceA_line}  {choiceA_column}]   Выбор Б: [{choiceB_line}  {choiceB_column}]\n")
            file2.write(f"Счёт игрока А = {field[choiceA_line][choiceA_column]}   Счёт игрока Б = {field[choiceB_line][choiceB_column]}\n")

averageA = amountA /count_games
averageB = amountB / count_games

ev_A = field[0][0] * 0.25 + field[0][1] * 0.25 + field[1][0] * 0.25 + field[1][1] * 0.25
ev_В = field[0][0] * 0.25 + field[0][1] * 0.25 + field[1][0] * 0.25 + field[1][1] * 0.25

quadratic_ev_A = field[0][0] ** 2 * 0.25 + field[0][1] ** 2 * 0.25 + field[1][0] ** 2 * 0.25 + field[1][1] ** 2 * 0.25
quadratic_ev_В = field[0][0] ** 2 * 0.25 + field[0][1] ** 2 * 0.25 + field[1][0] ** 2 * 0.25 + field[1][1] ** 2 * 0.25

varianceA = quadratic_ev_A - ev_A
varianceB = quadratic_ev_В - ev_В

deviationA = sqrt(varianceA)
deviationB = sqrt(varianceB)

with open("resultC.txt", "w", encoding="utf-8") as file:
    file.write(f"Среднее значение выигрыша/проигрыша игрока в одной игре = {(2-3-1+2)/4}\n"
               f"Среднее значение выигрыша/проигрыша игрока А за {count_games} игр = {averageA}\n"
               f"Среднее значение выигрыша/проигрыша игрока Б за {count_games} игр = {averageB}\n"
               f"Математическое ожидание игрока А = {ev_A}\n"
               f"Математическое ожидание игрока Б = {ev_В}\n"
               f"Среднее квадратическое отклонение игрока А = {deviationA}\n"
               f"Среднее квадратическое отклонение игрока Б = {deviationB}\n"
               f"Дисперсия игрока А = {varianceA}\n"
               f"Дисперсия игрока Б = {varianceB}")