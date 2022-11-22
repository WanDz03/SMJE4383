import csv

file = open("TitanicSurvival.csv")
data = list(csv.reader(file, delimiter=","))
file.close()

#for each_ele in data:
	#last_ele = each_ele[-1]
	#first_ele = each_ele[0]
	#print(last_ele)
data[-1].append('Good Person')

print(data[-1])
