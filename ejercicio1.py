import pandas as pd
import numpy as np

datos= {'Nombre': ['Leonardo', 'Joaquin', 'N/A', 'Paula', 'Enrique', 'Jhon'],
        'Materias': ['Lenguaje', 'EDF', 'Quimica', 'Matematicas', 'Ingles','N/A'],
        'Calificaciones': ['18','20', np.nan,'19' ,'16', '17'],
        'Deportes':['Futbol','Natacion', 'Tenis', 'Voley', 'N/A', 'Balon mano']
        }
df= pd.DataFrame(datos)
print(df)
print('n*4')

#DATOS NO VALIDOS

datos2 = {'Nombre': ['Leonardo', 'Joaquin', 'N/A', 'Paula', 'Enrique', 'Jhon'],
        'Materias': ['Lenguaje', 'EDF', 'Quimica', 'Matematicas', 'Ingles','N/A'],
        'Calificaciones': ['18','20', np.nan,'19' ,'16', '17'],
        'Deportes':['Futbol','Natacion', 'Tenis', 'Voley', 'N/A', 'Balon mano']
        }

df2 = pd.Dataframe(datos2)
print(df2)
print('/n'*1)
print(df2.info()) 