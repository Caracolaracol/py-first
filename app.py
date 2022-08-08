## FIRST PYTHON

## operaciones
x = 5/8
print(x)
y = 8-9+4*8-4 # 27

## VARIABLE
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

## receiving input
name = input("What is your name?")
print("Hello " + name) #string concatenation

#type conversion 
birth_year = input("Enter your birth year: ")
# age = 2020 - birth_year # python no sabe como restar un string y number. para corregir eso hay que usar la funcion int 
# print(age)
age = 2020 - int(birth_year)
print(age)


## conversores:
int()
float()
bool()
str()


## strings
course = 'Python for Begginers' # this is an object, string object. 
course.upper() # después del punto van los métodos. upper return un string con letras mayusculas
print(course.upper())
print(course.finde('y')) # buscara algo, 'y' el primer y que aparezca y dirá el index donde está la 'y'

#operadores logicos
numero = 10
numero > 5 and numero < 15 #true
numero > 5 and numero > 15 #false

palabra = 'Álvaro'
palabra == "Salir" or palabra == "Terminar" or palabra == "Exit" #false
palabra == "Salir" or palabra == "Álvaro" or palabra == "Exit" #true

## CONTROL STRUCTURES
if True:
    print('Imprimo esto porque la evaluacion fue verdadera') 

# prints both strings
Alvaro = 10
if Alvaro == 10:
    print('Alvaro Vale 67')
if Alvaro == 10:
    print('Alvaro Vale 10') 

# prints 'el resto no es cero'
alvaro = 13
if alvaro % 2 == 0:
    print ('el resto es 0')
else:
    print('el resto no es cero')

#prints 'Esto es algo cuando no da ningun resultado'
frase = "Alvaro"
if frase == "Entrar":
    print('Bienvenid@s')
elif frase == 'hola':
    print('nos estan saludando')
else:
    print('Esto es algo cuando no da ningun resultado')


## ejercicio
print('Elige tu propio camino')
inicio = input("Escribe empezar para iniciar el programa: ")
while (inicio == 'empezar'):
    print(""" ¿Que camino quieres elegir?
    escribe la opcion con numero
    1 - Quiero que me saludes
    2 - Deseo multiplicar ya que no se como hacerlo
    3 - quiero salir de este programa, ya que aprendi a multiplicar con el curso de Alvaro """)
    opcion = input()
    if opcion == '1':
        print("Te saludo")
    elif opcion == '2':
        numero1 = float(input('introduce el valor a multiplicar primero: '))
        numero2 = float(input('introduce el valor a multiplicar segundo: '))
        print('El resultado es: ', numero1*numero2)
    elif opcion == '3':
        print('Excelente decision que hayas tomado el curso de alvaro')
        break
    else:
        print('No se que elegiste, tuviste que haber puesto algun numero de las opciones, se nota que no tomaste el curso de alvaro')

## for

lista = [1,2,3,4,5,6,7,8,9]
indice = 0
while indice < len(lista):
    print(lista[indice])
    indice+=1 