#ejemplo de como cambiar palabras en strings
def replace_word():

    str = 'hola, soy samir y tengo 19 anos de edad'
    world_to_replace = input('enter the world to replace: ')
    world_replacement = input('enter the world replacement: ')
    print(str.replace(world_to_replace,world_replacement))

replace_word()