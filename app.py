from flask import Flask, render_template

app = Flask(__name__)

# 1. O PONTO DE PARTIDA (Página de Transparência/Originalidade)
@app.route('/')
def index():
    return render_template('index.html')

# 2. AVISO DO HOSPITAL (Segunda página)
@app.route('/aviso')
def aviso():
    return render_template('aviso.html')

# 3. TELA DE LOGIN
@app.route('/login')
def login():
    return render_template('login.html')

# 4. DASHBOARD (Painel Principal)
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# 5. CÂMERA ÉTICA
@app.route('/camera')
def camera():
    return render_template('camera.html')

if __name__ == '__main__':
    # Rode o site no modo debug para atualizar sempre que você salvar
    app.run(debug=True)