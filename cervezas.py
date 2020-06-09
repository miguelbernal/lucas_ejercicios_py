from requests_html import HTMLSession
import json

session = HTMLSession()
r = session.get("https://cervezapedia.com/beer/rate")
token = r.cookies["XSRF-TOKEN"]
print(token)
r = session.post("https://cervezapedia.com/beer/rate", headers={"X-XSRF-TOKEN": token})

datos = json.loads(r.content)

#print(datos)

for cerveza in datos["data"]:
        print("-------------------------------------------------------")
        print("Código:",cerveza['externalId'], "Nombre:",cerveza['name'])

        r = session.post("https://cervezapedia.com/beer/byId", headers={"X-XSRF-TOKEN": token}, json={"id" : cerveza['externalId']})
        datos_cerveza = json.loads(r.content)["data"]
        #print(datos_cerveza)
        print("Pais: ",datos_cerveza["countrySpanishName"])
        print("Alcohol: ",datos_cerveza["alcohol"])
        print("Estilo: ",datos_cerveza["styleName"])

        

