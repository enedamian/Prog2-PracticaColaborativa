import os
def existe_Archivo(nombre):
    if os.path.isfile(nombre):
        return True
    else:
        return False
def generar_lista_sin_signos(lista):
    lista_limpia=[]
    for palabra in lista:
        lista_limpia.append(palabra.strip(" ,.!¡¿?\n"))
    return lista_limpia

def generar_lista(nombre):
    if existe_Archivo(nombre):
        archivo = open(nombre,'r', encoding="utf-8")
        lista_palabras =[]
        for linea in archivo:
            lista_aux = linea.split(" ")
            lista_palabras += generar_lista_sin_signos(lista_aux)
        return lista_palabras
    else:
        return []
def contar_frecuencia_palabras(lista):
    dic_palabras = {}
    for palabra in lista:
        if palabra in dic_palabras:
            dic_palabras[palabra]+=1
        else:
            dic_palabras[palabra]=1
    return dic_palabras

def buscar_palabra_mas_frecuente(diccionario):
    fre_mayor=0
    llave_mayor=""
    for llave in diccionario:
        if diccionario[llave] > fre_mayor and len(llave)>2:
            fre_mayor = diccionario[llave]
            llave_mayor = llave
    return llave_mayor
def buscar_menos_frec(diccionario):
    fre_menor= 100000
    llave_menor=""
    for llave in diccionario:
        if diccionario[llave] < fre_menor and len(llave)>2:
            fre_menor = diccionario[llave]
            llave_menor = llave
    return llave_menor
def calcular_longitud_promedio(lista):
    suma=0
    for palabra in lista:
        suma += len(palabra)
    return int(suma/len(lista))

nombrearchivo= input("ingrese nombre del archivo: ")
lista_palabras = generar_lista(nombrearchivo)
dic_frecuencia_palabra= contar_frecuencia_palabras(lista_palabras)
palabra_mas_frec = buscar_palabra_mas_frecuente(dic_frecuencia_palabra)
palabra_menos_frec = buscar_menos_frec(dic_frecuencia_palabra)
promedio = calcular_longitud_promedio(lista_palabras)
print(f"Nombre del archivo: {nombrearchivo}\nLista de palabras:\n{lista_palabras}\nFrecuencia de las palabras:\n{dic_frecuencia_palabra}\nPalabra más frecuente: {palabra_mas_frec}\nPalabra menos frecuente: {palabra_menos_frec}\nLongitud promedio de las palabras: {promedio}")
