from flask import Flask, render_template, request, redirect, url_for
import json
import random
import string

app = Flask(__name__)

# Cargar o crear el archivo de almacenamiento de URLs
try:
    with open('urls.json', 'r') as file:
        urls = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    urls = {}

# Función para generar un código corto
def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

# Ruta principal
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['url']
        short_code = generate_short_code()
        urls[short_code] = original_url
        
        with open('urls.json', 'w') as file:
            json.dump(urls, file)
        
        return render_template('short.html', short_code=short_code)
    return render_template('index.html')

# Redirigir usando código corto
@app.route('/<short_code>')
def redirect_to_url(short_code):
    if short_code in urls:
        return redirect(urls[short_code])
    return "URL no encontrada", 404

if __name__ == '__main__':
    app.run(debug=True)
