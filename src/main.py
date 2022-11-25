from flask import Flask,render_template
from flask import jsonify
from documentos import documentos
from flask import request

def create_app():
    app=Flask(__name__)
    return app

app=create_app()

##################### CON EL METODO GET, OBTENGO DATOS.########

@app.route('/documentos', methods=['GET'])
def obtener_documentos():
    return jsonify(documentos)

@app.route('/documento/<id_documento>', methods=['GET'])
def obtener_paquete(id_documento):
    if (id_documento) in documentos:
        return jsonify( documentos[id_documento])
    else:
        return jsonify({"mensaje":"no existe el documento"})


############################ con el método POST, ############

@app.route('/documentos',methods=['POST'])
def agregar_documentos():

    nuevo_documento={"nombre":request.json['nombre'],
    "identificacion":request.json['identificacion'],
    "tipo_doc": request.json['tipo_doc'],
    "categoria":request.json['categoria'],
    "estado_doc" :request.json['estado_doc'],
    "precio":request.json['precio']
    }
    print( nuevo_documento)
    maximo=-1
    for x in documentos.keys():
        if int(x)>maximo:
            maximo=int(x)
    siguiente= maximo+1  
    
    documentos[str(siguiente)]=nuevo_documento
    with open('documentos.py','w') as data:
        data.write("documentos="+str(documentos))
        
    return jsonify(documentos)
  ############################# METODO PUT########################## 
  
  
@app.route('/documento/<id_documento>', methods=['PUT'])
def editar_documento(id_documento):
    documento_a_editar={"nombre":request.json['nombre'],
    "identificacion":request.json['identificacion'],
    "tipo_doc":request.json['tipo_doc'],
    "categoria":request.json['categoria'],
    "estado_doc":request.json['estado_doc'],
    "precio":request.json['precio']}
    documentos[str(id_documento)]=documento_a_editar
    
    
    with open('documentos.py','w') as data:
       data.write("documentos="+str(documentos))
       
    return "documento editado"
  
 ####################### METODO DELETE##########
 
@app.route('/documento/<id_documento>',methods=['DELETE'])
def borrar_paquete(id_documento):
    del documentos[id_documento]
    with open('documentos.py','w')as data:
        data.write("documentos="+str(documentos))
    return "documento " + id_documento + " borrado"

@app.route('/')
def index():
    return render_template('index.html',data=datos_inicio)


@app.route('/datos')
def datos():
    data={
        'titulo':'contacto'
    }
    return render_template('index.html',data = data)

datos_inicio={
    'titulo':'index',
'bienvenida':'Hola! desde html',
'etiqueta_2':'Somos el Grupo 4',

}


def pagina_no_encontrada(error):
    return render_template('404.html'), 404


             
if __name__ == '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port=5000)

