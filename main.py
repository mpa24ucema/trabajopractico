from flask import Flask, jsonify, request
from datos import medidas
from datos import cuadros_rsp
#from datos import cuadros
#from datos import imagen
from datos import cuadros_nuevos
app = Flask(__name__)



#ACA GENERAMOS LA API DE TERCEROS DE LA NASA
@app.route('/nasa', methods=['GET'])
def nasaGet():
    return jsonify({'cuadros:': cuadros_rsp, 'status': 'ok'})


#ACA HACEMOS QUE DE LA API DE LA NASA NOS TRAIGA ID Y IMAGEN
@app.route('/cuadros', methods=['GET'])
def imagenesGet():
    return jsonify({'imagenes disponibles:': cuadros, 'status': 'ok'})


#ACA EL CLIENTE ELIGE LA IMAGEN
@app.route('/imagen/<id>', methods=['GET'])
def imagenGet(id):
    return f'ID imagen:{id} \n '\
           f'Imagen: {imagen}' \



#ACA GENERAMOS LA TABLA DE MEDIDAS
@app.route('/medidas', methods=['GET'])
def medidasGet():
    return jsonify({'medidas:': medidas, 'status': 'ok'})




#ACA GENERAMOS EL CUADRO PERSONALIZADO

@app.route('/micuadro', methods=['POST'])
def miCuadroPost():
    id_post = request.json['id']
    medida_post = request.json['medida']
    cuadro_nuevo = {
        'id' : id_post,
        'medidas' : medida_post
    }
    cuadros_nuevos.append(cuadro_nuevo)
    return jsonify({'mensaje' : 'fue creado con exito', 'cuadro personalizado' : cuadros_nuevos})






#ESTO SIMEPRE VA AL FINAL!!
if __name__ == '__main__':
    app.run(debug=True, port=4000)


