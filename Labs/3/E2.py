'''
Description: Exercise 2 (file)
Version: 1.0.0.20210118
Author: Arvin Zhao
Date: 2021-01-18 17:40:41
Last Editors: Arvin Zhao
LastEditTime: 2021-01-18 18:33:30
'''

import os, random


file_name = 'QuizSummary.csv'
file = open(file_name, 'a')

if os.stat(file_name).st_size == 0:
    for header in ['Name', 'Question 1', 'Answer 1', 'Question 2', 'Answer 2', 'Score']:
        file.write(header + ',')

    file.write('\n\n')

summary = []
summary.append(input('Enter your name: ').strip())
score = 0

for count in range(2):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = str(num1) + ' + ' + str(num2) + ' = ?'
    summary.append(question)

    answer = int(input(question + '  '))
    summary.append(str(answer))

    if answer == num1 + num2:
        score += 50

summary.append(str(score))

for item in summary:
    file.write(item + ',')

file.write('\n')
file.close()