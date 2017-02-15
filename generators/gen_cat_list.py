
filename = "sickness_with_cat.txt"


cat_dict= dict()

with open(filename) as lines:
	for line in lines:
		data = line.replace("\n", "").split("\t")
		sickness = data[0]
		category = data[1]
		sickness_with_cat = data[2]

		if category not in cat_dict:
			cat_dict[category] = []
		cat_dict[category].append(sickness)

cats = list(cat_dict.keys())


# filtered means only categories with more than one sickness are included

filename0 = 'complete_cat_data.txt'
filename1 = 'cat_heirarchy.csv'
filename2 = 'filtered_cat_data.txt'
filename3 = 'cat_heirarchy_filtered.csv'

complete_data_file = open(filename0, 'a')
complete_heirarchy_file = open(filename1, 'a')
filtered_data_file = open(filename2, 'a')
filtered_heirarchy_file = open(filename3, 'a')

filtered_heirarchy_file.write('category,\n')

for c in cats:
	sicknesses = cat_dict[c]
	len_sick = len(sicknesses)

	if len_sick > 1:
		filtered_data_file.write( c + "\t")
		filtered_heirarchy_file.write('category.' +c + ",\n")
	complete_data_file.write(c + "\t")
	complete_heirarchy_file.write(c + "\n")

	for i in range(0,len_sick):
		s = sicknesses[i]

		end_tab = "\n"
		if i != (len_sick-1):
			end_tab = "\t"

		if len_sick > 1:
			filtered_data_file.write(s + end_tab)
			filtered_heirarchy_file.write('category.' +c+"."+s + ",1\n")
		complete_data_file.write(s + end_tab)
		complete_heirarchy_file.write(c+"."+s + ",1\n")

complete_heirarchy_file.close()
complete_data_file.close()
filtered_data_file.close()
filtered_heirarchy_file.close()

				






