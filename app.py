from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route("/loggedin", methods=['POST']) #autenticação de parâmetros de login
def login():
    usr = request.form['user']
    pswrd = request.form['password']
    # busca o usuario no banco de dados
    return render_template('logged.html', user=usr, password=pswrd)
    #return render_template("usuario.html") 

@app.route("/registered", methods=['POST'])
def register():
    usr = request.form['user']
    pswrd = request.form['password']
    return render_template('logged.html', user=usr, password=pswrd)

@app.route('/register')
def register_page():
    return render_template('register.html')

if __name__ == "__main__":
    app.run()