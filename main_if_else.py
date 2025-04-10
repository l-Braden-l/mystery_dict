
#Braden Leach
#January 22 2025
#Mystery Dictinary 

input_name = input('Please enter your students name: ')
#---Dict---#
names_dict = {
    "Smith":1234, 
    "Leach":1342, 
    "Lennon":5624
    }

while input_name not in names_dict: 
    print('Person is not in our system!')
    input_name = input('Please enter your students name: ')

else:
    print(f'{input_name}\'s Student ID is : {names_dict[input_name]}')


        
