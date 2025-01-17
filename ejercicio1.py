import pandas as pd
import numpy as np

datos= {'Nombre': ['Leonardo', 'Joaquin', 'Alex', 'Paula', 'Enrique', 'Jhon'],
        'Materias': ['Lenguaje', 'EDF', 'Quimica', 'Matematicas', 'Ingles','Historia'],
        'Calificaciones': ['18','20', '13','19' ,'16', '17'],
        'Deportes':['Futbol','Natacion', 'Tenis', 'Voley', 'Natacion', 'Balon mano']
        }
df= pd.DataFrame(datos)
print(df)