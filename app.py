from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicial():
    return render_template('inicial.html')

@app.route('/cardapio')
def cardapio():
    return render_template('cardapio.html')

@app.route('/avaliacoes')
def avaliacoes():
    return render_template('avaliacoes.html')

@app.route('/faleconosco')
def fale():
    return render_template('fale.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)