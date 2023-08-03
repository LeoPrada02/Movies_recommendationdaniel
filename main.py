'''
python -m uvicorn main:app --reload
'''

import pandas as pd
from fastapi import FastAPI


data = pd.read_csv('movies_dataset_clean.csv')

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Hello World"}



'''
def peliculas_idioma( Idioma: str ): Se ingresa un idioma (como están escritos en el dataset, no hay que traducirlos!). 
Debe devolver la cantidad de películas producidas en ese idioma. 
Ejemplo de retorno: X cantidad de películas fueron estrenadas en idioma
'''

@app.get('/lan/{idioma}')
async def peliculas_idioma(idioma: str):
    a = len(data[data['language'] == idioma])
    return f'{a} peliculas fueron estrenadas en {idioma}'


'''
def peliculas_duracion( Pelicula: str ): Se ingresa una pelicula. Debe devolver la duracion y el año.
Ejemplo de retorno: X . Duración: x. Año: xx
'''
@app.get('/{movie}')
async def peliculas_duracion(movie):
    d = data[['runtime', 'release_year']][data['title'] == movie]
    duracion = int(d['runtime'][1])
    anio = int(d['release_year'][1])
    return f'{movie}. Duracion: {duracion}min. Año: {anio}'


'''
def franquicia( Franquicia: str ): Se ingresa la franquicia, retornando la cantidad de peliculas, 
ganancia total y promedio Ejemplo de retorno: La franquicia X posee X peliculas, una ganancia 
total de x y una ganancia promedio de xx
'''
@app.get('/mov/{Franquicia}')
async def franquicia(Franquicia: str):
    collection = data[data['belongs_to_collection'] == Franquicia]
    numero = len(collection) 
    ganacia = collection['revenue'].sum()
    promedio = collection['revenue'].mean()
    return f'La franquicia {Franquicia} posee {numero} peliculas,una ganancia total de {ganacia} y una ganancia promedio de {promedio}'

'''
def peliculas_pais( Pais: str ): Se ingresa un país (como están escritos en el dataset, 
no hay que traducirlos!), retornando la cantidad de peliculas producidas en el mismo.
Ejemplo de retorno: Se produjeron X películas en el país X
'''

@app.get('/country/{pais}')
async def peliculas_pais(pais: str):
    collection = data[data['country'] == pais]
    num = len(collection)
    return f'Se produjeron {num} películas en el país {pais}'

'''
def productoras_exitosas( Productora: str ): Se ingresa la productora, 
entregandote el revunue total y la cantidad de peliculas que realizo.
Ejemplo de retorno: La productora X ha tenido un revenue de x 
'''

@app.get('/prod/{Productora}')
async def productoras_exitosas(Productora: str):
    collection = data[data['pro_comp1'] == Productora]
    num = len(collection)
    revenue = collection['revenue'].sum()
    return f'La productora {Productora} ha tenido un revenue de {revenue}, y realizo {num} peliculas'

'''
def get_director( nombre_director ): Se ingresa el nombre de un director 
que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido 
a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de 
lanzamiento, retorno individual, costo y ganancia de la misma, en formato lista. 
'''

@app.get('/dir/{director}')
async def get_director(director: str):
    collection = data[data['directores'] == director]
    exito = collection['return'].sum()
    v = []
    for i in range(len(collection)):
        w = []
        w.append(collection['title'][collection['title'].index[i]])
        w.append(collection['revenue'][collection['revenue'].index[i]])
        w.append(collection['budget'][collection['budget'].index[i]])
        w.append(collection['return'][collection['return'].index[i]])
        v.append(w)
    return f'exito del director: {exito} \n {v}' 