#analisisarlos datos tomados de los promedios diarios durante la semana en una empresa
#los cuales nos muestran
#temperatura del lugar
#porcentaje de contaminacion del aire
#total de desechos en kg
#consumo de agua en litros
#porcentaje de recuperacion de agua en lts
#importamos la libreria pandas 
import pandas as pd

#generamos los datos 
print("DATOS SEMANALES DE LA EMPRESA ")
datos=pd.read_excel("datosempresa.xlsx")

#creamos el dataf frame y lo mostramos 
datafra=pd.DataFrame(data=datos)
print(datafra)
print()
#con la funcion .median encontramos la mediana de cada variable 
print('mediana :')
print(datafra.median())
print()
#con la funcion .min encontramos el valor minimo de cada variable 
print('valor minimo :')
print(datafra.min())
print()
#con la funcion .max encontramos el valor maximo de cada variable 
print('valor maximo : ')
print(datafra.max())
print()
# con la funcion .std encontramos la desviacion estandar 
print('desviacion estandar :')
print(datafra.std())
print()
# .drescribe hace  una descripcion de los datos 
print('estudio datos :')
print(datafra.describe())
print()




