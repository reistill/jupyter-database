from flask import Flask, render_template, send_file
import sqlite3
import io

app = Flask(__name__)

# Função para conectar ao banco de dados e obter informações
def get_carros():
    conn = sqlite3.connect('uracan.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id_carro, modelo, preco FROM Carro")
    carros = cursor.fetchall()
    conn.close()
    return carros

# Rota para a página principal, onde os dados serão listados
@app.route('/')
def index():
    carros = get_carros()
    return render_template('index.html', carros=carros)

# Rota para exibir a imagem de uma pessoa
@app.route('/foto/<int:id_carro>')
def foto(id_carro):
    conn = sqlite3.connect('uracan.db')
    cursor = conn.cursor()
    cursor.execute("SELECT foto FROM Carro WHERE id_carro=?", (id_carro,))
    foto_blob = cursor.fetchone()[0]
    conn.close()

    # Enviar a imagem como resposta binária
    return send_file(io.BytesIO(foto_blob), mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
