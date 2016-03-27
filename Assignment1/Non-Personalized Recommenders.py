import csv
from Problem import Problem
reader = csv.reader(open("A1Ratings.csv","rU"))
problem=Problem()
for row in reader:
    problem.loadline(row)

average_ratings=dict(zip(problem.movienames,[('%.2f')%f for f in problem.meanRatings()]))
average_ratings=sorted(average_ratings.iteritems(),key=lambda d:d[1], reverse=True)
print average_ratings

most_ratings=dict(zip(problem.movienames,[f for f in problem.mostRatings()]))
most_ratings=sorted(most_ratings.iteritems(),key=lambda d:d[1],reverse=True)
print most_ratings

higher_ratings=dict(zip(problem.movienames,[('%.2f')%f for f in problem.rating4()]))
higher_ratings=sorted(higher_ratings.iteritems(),key=lambda d:d[1],reverse=True)
print higher_ratings

rel=dict(zip(problem.movienames[1:],[('%.2f')%f for f in problem.getRelevance()]))
rel=sorted(rel.iteritems(),key=lambda d:d[1],reverse=True)
print rel