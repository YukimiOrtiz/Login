from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    nombre = request.form['nombre']
    correo = request.form['email']
    password = request.form['password']
    
    return render_template('user.html', nombre=nombre, correo=correo, password=password)

if __name__ == "__main__":
    app.run( debug=True)