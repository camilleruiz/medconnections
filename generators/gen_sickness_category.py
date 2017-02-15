
filename = "category/categories_raw.csv"

new_file = "sickness_with_cat.txt"

w = open(new_file, "a")

with open(filename) as lines:
	for line in lines:
		data = line.replace("\n", "").split(",")

		sickness = data[1]
		category = data[3].replace("\"", "")

		if category == "":
			if data[5] == data[8] and data[8] == data[10]:
				category = data[5].replace("\"", "")

		if category != "" and category != "-1" and category != "-2":
			w.write(sickness + "\t" + category +"\t" + category+"."+sickness + "\n")

w.close()


