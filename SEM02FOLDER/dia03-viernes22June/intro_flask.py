from flask import Flask

# Instancia
app=Flask(__name__)


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


# levantamos nuestro servidor para que se quede a la espera
# de posibles peticiones de un tiempo indeterminado

#   debug (valor por defecto es False)
    # 
app.run(debug=True)