'''
Напишите программу для печати всех уникальных
значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
'''

list_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
	             {"VI": "S005"}, {"VII": " S005 "}, 
	             {" V ":" S009 "}, {" VIII ":" S007 "}]

unique_dict_items = set()
for i in list_dict:
	for j in i.keys():
	    unique_dict_items.add(i[j])
print(unique_dict_items)

                            # Second Employment
new_list = [list(i.values())[0].strip() for i in list_dict]
print(set(new_list))
