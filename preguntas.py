"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.
"""
def pregunta_01():
        with open( 'data.csv' , "r") as file:
            data = file.readlines()
            
        data = [row.replace("\n", "") for row in data]
        data = [row.replace("\t", ",") for row in data]
        data = [row.split(",") for row in data]
        data = [row[1] for row in data]
        data = [int(row) for row in data]
        answer = sum(data)
        
        return answer
""""
    Retorne la suma de la segunda columna.
  
    """
def pregunta_02():

    import collections
    from collections import Counter

    with open( 'data.csv' , "r") as file:
                data = file.readlines()
            
    data = [row.replace("\n", "") for row in data]
    data = [row.replace("\t", ",") for row in data]
    data = [row.split(",") for row in data]
    data = [row[0] for row in data]
    a = Counter(data)
    answer= list(a.items())
    answer.sort(reverse=False)
    return answer


    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """

def pregunta_03():

    with open( 'data.csv' , "r") as file:
        data = file.readlines()
        
    data = [row.replace("\n", "") for row in data]
    data = [row.replace("\t", ",") for row in data]
    data = [row.split(",") for row in data]
    data = [row[0:2] for row in data]
    data = [(row[0], int(row[1])) for row in data] 
    answer =[(k, sum([y for (x,y) in data if x == k])) for k in dict(data).keys()]
    answer.sort(reverse = False)
    return answer

    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.
    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]
    """
    with open( 'data.csv' , "r") as file:
        data = file.readlines()    
        
    months = [data[i][2][5:7] for i in range(len(data))]
    answer = []

    for month in months:
        answer.append((month,months.count(month)))

    answer = sorted(list(set(answer)))
    
    return answer
    


    """"""
def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.
    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]
    """
    with open( 'data.csv' , "r") as file:
        data = file.readlines()    
        
    col_0 = [data[i][0] for i in range(len(data))]
    col_1 = [int(data[i][1]) for i in range(len(data))]
    unique_characters = sorted(list(set(col_0)))
    answer = []

    for character in unique_characters:
        max1 = min(col_1)
        min1 = max(col_1)
        for i in range(len(data)):
            if col_0[i] == character:
                if col_1[i] > max:
                    max = col_1[i]    
                if col_1[i] < min:
                    min = col_1[i]
        answer.append((character,max,min))

    return answer
    """"""""

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.
    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]
    """
    with open( 'data.csv' , "r") as file:
        data = file.readlines()

    data = [row.replace("\n", "") for row in data]
    data = [row.replace("\t", ",") for row in data]
    data = [row.split(",") for row in data]
        
    dict_min = {}
    dict_max = {}

    for row in data:
        for element in data:
            key = element[:3]
            value = int(element[4:])
            if key in dict_min:
                if value < dict_min[key]:
                    dict_min[key] = value
            elif key not in dict_min:
                dict_min[key] = value
            if key in  dict_max:
                if value >  dict_max[key]:
                     dict_max[key] = value
            elif key not in  dict_max:
                 dict_max[key] = value           

    list_result =[]
    for result in zip(dict_min.keys(),list(dict_min.values()),list(dict_max.values())):
            list_result.append(result)
            list_result.sort(key = lambda x: x[0])
    return list_result