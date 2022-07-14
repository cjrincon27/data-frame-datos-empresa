 
#iIMPORTAMOS LIBRERIA PANDAS
import pandas as pd
#generamos los datos 
print("MEDIDAS DEL RIO 24 HORAS   ")
MEDIDAS=pd.Series([27,22,28,39,30,23,24,22,23,24,45,45,44,44,44,44,23,46,47,47,48,40,94,40])
#IMPRIMIMOS LAS MEDIDAS SERIE
print(MEDIDAS)
#CALCULAMOS LA MEDIDA EN METROS
M=MEDIDAS/100
print(M)
#MAYOR MEDIDA EN METROS .MAX
print('MAYOR MEDIDA EN METROS :')
print(M.max())
#MENOR MEDIDA EN METROS.MIN
print('MENOR MEDIDA EN METRO :')
print(M.min())







         







