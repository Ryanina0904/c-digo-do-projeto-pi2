from flask import Flask, render_template, request, redirect, url_for,flash, session, jsonify
from flask import session
import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['DATABASE'] = 'usuarios.db'
app.config['JSON_AS_ASCII'] = False
app.secret_key = 'chave_secreta'

conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'usuarios.db'))

def init_db():
    with app.app_context():
        criar_tabelas()

@app.errorhandler(500)
def internal_server_error(error):
    print(f"Erro interno do servidor: {error}")
    return jsonify({"mensagem": "Erro interno do servidor"}), 500


def conectar_bd():
    return sqlite3.connect(app.config['DATABASE'])

def criar_tabelas():
    with conectar_bd() as conexao:
        cursor = conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                senha TEXT NOT NULL
            )
        ''')
        conexao.commit()

# Inicializa o banco de dados
criar_tabelas()
#usuarios
def adicionar_usuario(email, senha):
    # Criar a conexão com o banco de dados
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    # Verificar se o e-mail já existe
    cursor.execute('SELECT * FROM usuario WHERE email = ?', (email,))
    usuario_existente = cursor.fetchone()

    if usuario_existente:
        print(f"O e-mail {email} já está cadastrado no banco de dados.")
    else:
        # Hash da senha antes de armazenar
        senha_hash = generate_password_hash(senha, method='pbkdf2:sha256')


        # Inserir o novo usuário na tabela (permitindo valor nulo para 'nome')
        cursor.execute('INSERT INTO usuario (nome, email, senha) VALUES (?, ?, ?)', ('Nome do Usuário', email, senha_hash))
        conn.commit()
        print(f"Usuário {email} adicionado com sucesso!")

    # Fechar a conexão
    conn.close()

# Exemplo de uso
adicionar_usuario('email','senha')

#html/css
def listar_arquivos_html(templates):
    arquivos_html = []
    for pasta_atual, subpastas, arquivos in os.walk(templates):
        for arquivo in arquivos:
            if arquivo.endswith('.html'):
                caminho_completo = os.path.join(pasta_atual, arquivo)
                arquivos_html.append(caminho_completo)
    return arquivos_html

def listar_arquivos_css(static):
    arquivos_css = []
    for pasta_atual, subpastas, arquivos in os.walk(static):
        for arquivo in arquivos:
            if arquivo.endswith('.css'):
                caminho_completo = os.path.join(pasta_atual, arquivo)
                arquivos_css.append(caminho_completo)
    return arquivos_css


@app.route('/listar_html_css')
def listar_html_css():
    # Caminho para as pastas 'templates' e 'static'
    caminho_templates = os.path.join(os.path.dirname(__file__), 'templates')
    caminho_static = os.path.join(os.path.dirname(__file__), 'static')

    # Lista de todos os arquivos HTML na pasta 'templates'
    arquivos_html = listar_arquivos_html(caminho_templates)

    # Lista de todos os arquivos CSS na pasta 'static'
    arquivos_css = listar_arquivos_css(caminho_static)

    # Renderiza uma página mostrando a lista de arquivos HTML e CSS
    return render_template('listagem_arquivos.html', arquivos_html=arquivos_html, arquivos_css=arquivos_css)

@app.route('/')
def index():
    return render_template('home.html')



# rota cadastro
@app.route('/cadastrar', methods=['POST'], endpoint='cadastrar_usuario')
def cadastrar():
    try:
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        # Hash da senha antes de armazenar no banco de dados
        senha_hash = generate_password_hash(senha, method='pbkdf2:sha256')

        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()

        # Verifica se o e-mail já está cadastrado
        cursor.execute('SELECT * FROM usuario WHERE email = ?', (email,))
        if cursor.fetchone():
            conn.close()
            return jsonify({"success": False, "message": "E-mail já cadastrado. Por favor, escolha outro e-mail."})

        # Insere o novo usuário no banco de dados
        cursor.execute('INSERT INTO usuario (nome, email, senha) VALUES (?, ?, ?)', (nome, email, senha_hash))

        conn.commit()
        conn.close()

        print(f'Usuário cadastrado: Nome: {nome}, E-mail: {email}, Senha: {senha_hash}')

        # Redireciona para a página home após o cadastro bem-sucedido
        return redirect(url_for('home'))

    except Exception as e:
        # Log de exceção
        print(f"Erro durante o cadastro: {str(e)}")
        return jsonify({"success": False, "message": "Erro durante o cadastro. Por favor, tente novamente."})

@app.route('/cadastro', methods=['GET'])
def exibir_formulario_cadastro():
    return render_template('cadastro.html')

# Rota para processar o login
@app.route('/login', methods=['GET'])
def exibir_pagina_login():
    return render_template('login.html')

@app.route('/login', methods=['POST'], endpoint='login_usuario')
def login():
    try:
        email = request.form.get('email')
        senha_digitada = request.form.get('senha')

        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM usuario WHERE email = ?', (email,))
        usuario = cursor.fetchone()

        conn.close()

        if usuario and check_password_hash(usuario[3], senha_digitada):
            print("Login bem-sucedido")
            return jsonify({"success": True, "message": "Login bem-sucedido."})
        else:
            print("Credenciais inválidas")
            return jsonify({"success": False, "message": "Credenciais inválidas. Por favor, verifique seu e-mail e senha."})

    except Exception as e:
        print(f"Erro durante o login: {str(e)}")
        return jsonify({"success": False, "message": "Erro durante o login. Por favor, tente novamente."})




#instrutores
@app.route('/Instrutores')
def exibir_instrutores():
    # Você pode recuperar dados de instrutores do banco de dados ou de outra fonte
    instrutores = [
        {"nome": "Instrutor 1", "descricao": "Descrição do Instrutor 1"},
        {"nome": "Instrutor 2", "descricao": "Descrição do Instrutor 2"},
        # Adicione mais instrutores conforme necessário
    ]

    return render_template('Instrutores.html')

# home page
@app.route('/home')
def home():
    return render_template('home.html')



if __name__ == '__main__':
    init_db()
    app.run(debug=True)
    
    

