import pandas as pd
df= pd.read_csv('data/sepomex.csv')
#busqueda de colonias usando CP
df1=df[(df["d_CP"]==1401) & (df["d_tipo_asenta"]=="Colonia")]  
#CP= df[(df["d_CP"]==1401) and (df["d_tipo_asentaa"]=="Colonia")] 
##print(df1[["d_asenta","d_estado"]])


##### busqueda de colonias, municipios , estados por nombres
# d_estado, D_mnpio, d_asenta
# d_tipo_asenta
estado=input("Escribe una palabra")
colonia=input("Escribe una palabra")
df2=df[df["d_estado"].str.startswith(estado,na=False)]
df3=df2[df2["D_mnpio"].str.startswith(colonia,na=False)]
print(df3[["d_estado","D_mnpio"]])
