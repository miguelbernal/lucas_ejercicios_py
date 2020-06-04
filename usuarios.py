datos = []

while True:
    nombre = input('Nombre: ')
    if nombre == '': # para salir del programa se deja el nombre vacio
        break
    edad = input('Edad: ') # esto me retorna un string
    clave = input('Contraseña: ')
    # Validacion de espacios al comienzo y al final
    ok = True
    if (nombre[0] == ' '): # Comienzo es igual a espacio
        ok = False # ok ponemos a falso para no grabar los datos
        print('Nombre empieza con espacio')
    if (nombre[len(nombre)-1] == ' '): # Final es igual a espacio
        ok = False
        print('Nombre termina con espacio')
    if (edad[0] == ' '):
        ok = False
        print('Edad empieza con espacio')
    if (edad[len(edad)-1] == ' '):
        ok = False
        print('Edad termina con espacio')
    if (clave[0] == ' '):
        ok = False
        print('Contraseña empieza con espacio')
    if (clave[len(clave)-1] == ' '):
        ok = False
        print('Contraseña termina con espacio')
    # Validar solo alfanumericos
    if (not nombre.isalnum()): # da verdadero si es alfanumerico
        ok = False
        print("El nombre no es alfanumerico")
    # Validar edad de 1 a 100
    if (int(edad) < 1 or int(edad) > 100): # valida la edad convertida a entero
        ok = False
        print("Edad debe ser mayor a 1 y menor o igual a 100")
    # Validar contraseña
    if (len(clave) < 8 ): # la longitud de la clave si es menor a 8 da error
        ok = False
        print("Longitud de la contraseña debe ser como minimo 8")
    numero = False
    letra = False
    mayuscula = False
    for i in range(0,len(clave)): # recorremos cada letra de la clave
        if(clave[i].isnumeric()): # si la letra es numerica
            numero = True
        if(clave[i].isalpha()): # si la letra es una letra
            letra = True
            if(clave[i].isupper()): # si la letra es mayuscula 
                mayuscula = True
    print(numero, letra, mayuscula)
    if( not (numero and letra and mayuscula)): # Si no tiene un numero y una letra y una mayuscula da error
        ok = False
        print("La contraseña debe contener numeros, letras y mayusculas")
    if (ok): # si la validacion fue correcta
        existe = False
        for dato in datos: # verifica si el nombre ya existe en datos
            if (dato["nombre"] == nombre):
                existe = True
                print('El usuario ya existe')
                break
        if (not existe): # si no existe agrega los datos
            diccionario = {'nombre' : nombre, 'edad' : edad, 'clave': clave }
            datos.append(diccionario) # agregar el diccionario a datos
            for dato in datos: # imprime los datos
                print(dato)
    
print('Gracias registrar su usuario')