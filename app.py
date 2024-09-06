from flask import Flask
import psycopg2
from flask import render_template 


conn = psycopg2.connect(
    dbname="abrigo_animais",
    user="postgres",      
    password="magog789",  
    host="localhost"           
)

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Animal Shelter!'

from flask import request 

@app.route('/add_animal', methods=['POST'])
def add_animal():
    if request.method == 'POST':
        nome = request.form['nome']
        especie = request.form['especie']
        raca = request.form['raca']
        idade = request.form['idade']
        necessidades_alimentares = request.form['necessidades_alimentares']

        with conn.cursor() as cur:
            cur.execute('''
                INSERT INTO Animal (nome, especie, raca, idade, necessidades_alimentares) 
                VALUES (%s, %s, %s, %s, %s)
            ''', (nome, especie, raca, idade, necessidades_alimentares))
        conn.commit()

        return 'Animal added successfully!'

    # Handle GET requests or errors here if needed

# Route to handle Alimento form submission
@app.route('/add_alimento', methods=['POST'])
def add_alimento():
    if request.method == 'POST':
        nome = request.form['nome']
        marca = request.form['marca']
        categoria = request.form['categoria']
        data_validade = request.form['data_validade']
        quantidade_estoque = request.form['quantidade_estoque']

        with conn.cursor() as cur:
            cur.execute('''
                INSERT INTO Alimento (nome, marca, categoria, data_validade, quantidade_estoque) 
                VALUES (%s, %s, %s, %s, %s)
            ''', (nome, marca, categoria, data_validade, quantidade_estoque))
        conn.commit()

        return 'Alimento added successfully!'

    # Handle GET requests or errors here if needed

# Route to handle Doador form submission
@app.route('/add_doador', methods=['POST'])
def add_doador():
    if request.method == 'POST':
        nome = request.form['nome']
        contato = request.form['contato']

        with conn.cursor() as cur:
            cur.execute('''
                INSERT INTO Doador (nome, contato) 
                VALUES (%s, %s)
            ''', (nome, contato))
        conn.commit()

        return 'Doador added successfully!'

    # Handle GET requests or errors here if needed

if __name__ == '__main__':
    app.run(debug=True)