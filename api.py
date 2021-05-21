from flask import Flask, request, render_template, make_response
from flask  import jsonify
from flask import json
import pandas as pd

# leer el archivo csv sepomex en el cual estan contenidos los datos de los 32 estados "
# el archivo esta contenido en la carpeta data en este mismo proyecto
df=pd.read_csv('data/sepomex.csv')


app = Flask(__name__)




# el template que se uso se encuentra en  la carpeta template 
@app.route('/')
def home():
    return make_response(render_template('index.html'))


@app.route('/opciones',methods =["POST","GET"])
def busqueda():
    if request.method=='POST':  
        estado = request.form["estado"]
        municipio = request.form["municipio"]
        colonia = request.form["colonia"]
        # se usa la biblioteca pandas para filtrar la informacion dependiendo de la palabra que escriba el usuario, 
        # startswith arrojara las palabras empieze exactamente igual como esta en el dataset es decir si inicia con mayuscula se debe poner con mayuscula ya que generara un error se pone
        # todo con minusculas  y esta en el dataset como mayusculas 
        df1=df[df["d_estado"].str.startswith(estado,na=False)]
        df2=df1[df1["D_mnpio"].str.startswith(municipio,na=False)]
        df3=df2[(df2["d_asenta"].str.startswith(colonia,na=False)) & (df["d_tipo_asenta"]=="Colonia")]
        # se convierte el csv en json para ser consumido por la api
        # se carga el dataset en la ruta /opciones despues de escribir los parametros a filtrar en los campos de colonia, estado y municipio
        data= df3.to_json(orient="records")
        parsed = json.loads(data)
    
        return make_response(jsonify(parsed))
    


if __name__ == '__main__':
    app.run(debug = True)