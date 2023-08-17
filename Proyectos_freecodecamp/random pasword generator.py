#generar contrasena si el usuario lo desea, generar contrasena segun la longitud deseada
#en caso de no, salir

import string
import random

characters = list(string.ascii_letters + string.digits + '!@#$%^&*')

def generate_password():
    password_lenght = int(input("how long do you want your password: "))

    random.shuffle(characters)

    password = []

    for x in range(password_lenght):
        password.append(random.choice(characters))

    random.shuffle(characters)

    password = "".join(password)

    print(password)

valor = int(input('press 1 if you want a new password, any other character to not have one: '))

if valor == 1:
    generate_password()
else:
    print('see you later')