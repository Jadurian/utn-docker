from flask import Flask, request

app = Flask(__name__)

@app.route('/mi_endpoint', methods=['GET'])
def mi_endpoint():
    # Obtiene el valor del parámetro 'ABC' en la URL
    abc_value = request.args.get('ABC')
    
    # Verifica si el valor de 'ABC' es '123'
    if abc_value == '123':
        return "XYZ"
    else:
        return "Valor incorrecto", 400  # Código de error si el valor no es correcto

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)