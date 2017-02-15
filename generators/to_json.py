import operator
import random

def remove_symptom(connections, rem_name):
	names = connections.keys()
	for n in names:
		symptoms = connections[n]

		new_symptoms = []
		for s in symptoms:
			if s != rem_name:
				new_symptoms.append(s)

		connections[n] = new_symptoms
	return connections
file_name = "byoumei.txt"
sickness_with_cat = "sickness_with_cat.txt"
# file_name = "tester.txt"
new_file = "medical_connections_test.json"



sick_with_cat = dict()

with open(sickness_with_cat) as lines:
	for line in lines:
		data = line.replace("\n","").split("\t")
		sick_with_cat[data[0]] = data[2] + "(" + data[1] + ") "

connections = dict()

c = 0
with open(file_name) as f:
	for line in f:

		split_data = line.replace('\n','').split('\t')
		name = split_data[0]
		imports = split_data[1].split(',')

		if name not in sick_with_cat:
			continue
		name = sick_with_cat[name]

		if name not in connections:
			connections[name] = []

		for i in imports:
			if len(i) > 0:
				if i not in sick_with_cat:
					continue
				i = sick_with_cat[i]

				if i not in connections:
					connections[i] = []
				connections[name].append(i)

w = open(new_file, "a")



final_connections = dict()
names = random.sample(list(connections.keys()), 300)
# names = list(connections.keys())
print(len(names))

for name in names:
	symptoms = connections[name]

	if len(symptoms) > 0:
		final_connections[name] = symptoms

names = final_connections.keys()
for name in names:
	symptoms = final_connections[name]

	new_symptoms = []
	for s in symptoms:
		if s != name and s in names:
			new_symptoms.append(s)

	final_connections[name] = new_symptoms

names = list(final_connections.keys())
labels = []
for name in names:
	symptoms = final_connections[name]
	significance = 0

	for k in names:
		if k in final_connections.keys() and name in final_connections[k]:
			significance += 1 

	if len(symptoms) == 0 and significance == 0:
		final_connections.pop(name)
		continue

	if significance > len(symptoms):
		labels.append("illness." + name)
	else:
		labels.append("symptom." + name)

names = list(final_connections.keys())
print(len(names))
print(len(labels))

w.write("[")
c = 0

names = final_connections.keys()
for name in names:
	symptoms = final_connections[name]

	# main_sicknesses.append(name)
	if c == 1:
		to_write =",\n{\"name\":\"" + name + "\",\"imports\":["
	if c == 0:
		to_write ="\n{\"name\":\"" + name + "\",\"imports\":["
		c = 1

	a = 0
	for s in symptoms:
		to_write += "\"" + s + "\","
		a = 1
		# possibly_print_empty.append(s)

	if a == 1:
		to_write = to_write[:-1] + "]}"
	else:
		to_write += "]}"
	w.write(to_write)

# for s in possibly_print_empty:
# 	if s not in main_sicknesses:
# 		to_write = ",\n{\"name\":\"" + s + "\",\"imports\":[]}"
# 		w.write(to_write)

w.write("\n]")
w.close()



