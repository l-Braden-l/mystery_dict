
#Braden Leach
#January 22 2025
#Mystery Dictinary 

input_name = input('Please enter a name: ')

#---Dict---#
names_dict = {"Smith":1234, "Leach":1342, "Lennon":5624}

#---Print---#
print(f'Smith : {names_dict["Smith"]}')
print(f'Leach : {names_dict["Leach"]}')
print(f'Lennon : {names_dict["Lennon"]}')

#---If not in dict---#
unknown_names = names_dict.get('John','Requested key not found!')
print(f"David : {unknown_names}")
print()



if input_name not in names_dict:
    print('Requested key not found!') 
