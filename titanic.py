import csv

file = open("TitanicSurvival.csv")
data = list(csv.reader(file, delimiter=","))
file.close()

print(data[-10:-1])
