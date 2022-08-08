age = 20
# con punto se escriben los deciamles
price = 19.95
# string value, # es buena practica usar guion bajo
first_name = "Mosh"
is_online = False # boolean value
print(age)
# exercise:
name = "john Smith"
age = 20
new_patient = True

# receiving input

name = input("What is your name?")
print("Hello " + name) #string concatenation

#type conversion 
birth_year = input("Enter your birth year: ")
# age = 2020 - birth_year # python no sabe como restar un string y number. para corregir eso hay que usar la funcion int 
# print(age)

age = 2020 - int(birth_year)
print(age)

# conversores:
int()
float()
bool()
str()