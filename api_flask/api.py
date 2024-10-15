from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Caminho csv
caminho_dados = r'C:\Users\dudaf\flask_api_data\api_flask\tipos.csv'

tipos_df = pd.read_csv(caminho_dados)

# Rota para a página inicial
@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'message': 'Bem-vindo à API! Use /tipos/<id> para consultar um tipo.',
        'exemplo': '/tipos/1'
    }), 200

# Rota API para retornar os tipos
@app.route('/tipos/<int:id>', methods=['GET'])
def get_tipo(id):
    global tipos_df
    tipo = tipos_df.loc[tipos_df['id'] == id, 'nome'].values
    if tipo:
        return jsonify({'id': id, 'tipo': tipo[0]}), 200
    else:
        return jsonify({'error': 'Tipo não encontrado'}), 404

# Iniciar o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
    