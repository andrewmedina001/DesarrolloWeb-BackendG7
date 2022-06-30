from flask import Flask, request
from datetime import datetime
from flask_cors import CORS
# 
# Instancia de clase
    # __name__ <-- variable propia de python que muestra si el archivo que estamos utilizando 
    #   es el archivo principal del proyecto, si es el archivo principal su valor era '__name__',
    # caso contraio indicara otro valor
app=Flask(__name__)
CORS(app)
productos=[]
#Creacion de un Endpoint
#   1. Usando decorador con @
        # Un decorador es un patron de software que se utiliza para modificar el 
        # comportamiento de un metodo de una clase sin la necesidad de emplear
        # otros metodos como la herencia, tampoco es necesario modificar el 
        # comportamiento de dicha clase
@app.route('/')
def rutaInicial():
    print('Ingreso al EndPoint Inicial')
    return 'Bienvenido a tu primera API de CodiGo' 

@app.route('/state')
def ruta02():
    return {
        'hora':datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

@app.route('/producto', methods=['POST'])
def gestionProductos():
    # get_json() > convierte el json que el cliente envia a un diccionario para que python lo pueda entender
    print(request.get_json())
    producto = request.get_json()
    productos.append(producto)
    return {
        'message': 'Producto creado exitosamente',
        'content': producto
    }


@app.route('/devolver-productos', methods=['GET'])
def devolverProductos():
    return {
        'message': 'Los productos son',
        'content': productos
    }

# levantamos nuestro servidor para que se quede a la espera
# de posibles peticiones de un tiempo indeterminado

#   debug (valor por defecto es False)
    # 
app.run(debug=True)