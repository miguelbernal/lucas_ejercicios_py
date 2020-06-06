from requests_html import HTMLSession

def col(texto, cantidad, derecha):
    if derecha:
        texto = texto + " "*(cantidad - len(texto))
    else:
        texto = " "*(cantidad - len(texto)) + texto
    return texto

session = HTMLSession()
r = session.get('https://bcp.gov.py/webapps/web/cotizacion/monedas')
datos = r.html.find('#dp_cotizacion',first=True)
fecha = datos.attrs['value']

datos = r.html.find('#cotizacion-interbancaria',first=True)
tabla = datos.text.split('\n')
contador = 0
linea = ""
veces = 0;
for elemento in tabla:
    contador += 1
    if contador == 2:
        linea += col(elemento,63, True) + " | "
    else:     
        linea += col(elemento,30, True) + " | "
    if contador == 1:
        print(col(linea.replace('|',''),100,False))
        linea = ""
    if contador == 4:
        print(linea)
        linea = ""
    if contador > 4:
        veces += 1 
    if contador >= 8:
        if veces == 4:
            print(linea)
            linea = ""
            veces = 0



