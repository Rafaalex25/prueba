import pandas as pd
from pandas import read_excel

### como el archivo bajado de la pagina en cada hoja del excel contiene informacion de cada estado
## se procede a concatenar los archivos en un solo archivo y se converte a un archivo csv, se manda aguardaar en la carpeta de nombre data

### se converte a csv para dismunuir el tamanio del archivo en formato excel

df1=pd.read_excel('data/CPdescarga.xls', sheet_name=1)
df2=pd.read_excel('data/CPdescarga.xls', sheet_name=2)
df3=pd.read_excel('data/CPdescarga.xls', sheet_name=3)
df4=pd.read_excel('data/CPdescarga.xls', sheet_name=4)
df5=pd.read_excel('data/CPdescarga.xls', sheet_name=5)
df6=pd.read_excel('data/CPdescarga.xls', sheet_name=6)
df7=pd.read_excel('data/CPdescarga.xls', sheet_name=7)
df8=pd.read_excel('data/CPdescarga.xls', sheet_name=8)
df9=pd.read_excel('data/CPdescarga.xls', sheet_name=9)
df10=pd.read_excel('data/CPdescarga.xls', sheet_name=10)
df11=pd.read_excel('data/CPdescarga.xls', sheet_name=11)
df12=pd.read_excel('data/CPdescarga.xls', sheet_name=12)
df13=pd.read_excel('data/CPdescarga.xls', sheet_name=13)
df14=pd.read_excel('data/CPdescarga.xls', sheet_name=14)
df15=pd.read_excel('data/CPdescarga.xls', sheet_name=15)
df16=pd.read_excel('data/CPdescarga.xls', sheet_name=16)
df17=pd.read_excel('data/CPdescarga.xls', sheet_name=17)
df18=pd.read_excel('data/CPdescarga.xls', sheet_name=18)
df19=pd.read_excel('data/CPdescarga.xls', sheet_name=19)
df20=pd.read_excel('data/CPdescarga.xls', sheet_name=20)
df21=pd.read_excel('data/CPdescarga.xls', sheet_name=21)
df22=pd.read_excel('data/CPdescarga.xls', sheet_name=22)
df23=pd.read_excel('data/CPdescarga.xls', sheet_name=23)
df24=pd.read_excel('data/CPdescarga.xls', sheet_name=24)
df25=pd.read_excel('data/CPdescarga.xls', sheet_name=25)
df26=pd.read_excel('data/CPdescarga.xls', sheet_name=26)
df27=pd.read_excel('data/CPdescarga.xls', sheet_name=27)
df28=pd.read_excel('data/CPdescarga.xls', sheet_name=28)
df29=pd.read_excel('data/CPdescarga.xls', sheet_name=29)
df30=pd.read_excel('data/CPdescarga.xls', sheet_name=30)
df31=pd.read_excel('data/CPdescarga.xls', sheet_name=31)
df32=pd.read_excel('data/CPdescarga.xls', sheet_name=32)

frames=[df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,
        df11,df12,df13,df14,df15,df16,df17,df18,df19,df20,
        df21,df22,df23,df24,df25,df26,df27,df28,df29,df30,
        df31,df32]
result=pd.concat(frames)
result.to_csv('data/sepomex.csv')

#print(len(result.axes[0]))