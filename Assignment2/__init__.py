import csv
from Problem import Problem
reader=csv.reader(file("Assignment 2.csv","rb"))#xls format has problem
problem=Problem()
index=-1

for row in reader:
    problem.loadLine(index,row)
    index+=1
# print(problem.matrix)
# print problem.user1
# print problem.user2
# print problem.attributes
# #Part1
# problem.computeProfile()
# problem.predictuser1()
# problem.predictuser2()
#Part2
# problem.normalize()
# problem.computeProfile()
# problem.predictuser1()
# problem.predictuser2()

#Part3
problem.computeDF()
