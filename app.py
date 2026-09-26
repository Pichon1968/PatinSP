from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    informacion_profesora = {
"nombre": "Belen Profesora de Patin Artistico",
"descripcion": "Clases para niñ@s y Adolescentes ",
"niveles": [
"Iniciación",
"Intermedio",

"Competición"
],
"contacto": "5491140625114",
"ubicacion": "Ateneo San Pantaleon San Teodosio"
}


    return render_template(
    'index.html',
    datos=informacion_profesora
)

if __name__ == '__main__':
    app.run(debug=False)
