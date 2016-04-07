import csv
from Problem import Problem
reader=csv.reader(file("Assignment 3.csv","rb"))
problem=Problem()
index=0
for row in reader:
    problem.loadline(row,index)
    index+=1
# print problem.users
# print problem.movies
# print problem.matrix
#Without Normalization
problem.computecorelation()
problem.calcuNearneibor()
#test 3712(7th)
#problem.predict(6)
#predict movies for 3867(5th) and 89(14th)
problem.predict(4)
problem.predict(13)
#Normalization
problem.predictnormalized(4)
problem.predictnormalized(13)