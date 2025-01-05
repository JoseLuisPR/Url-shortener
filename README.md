# Acortador de Enlaces (Link Shortener)

Este es un simple **acortador de enlaces** desarrollado con **Flask**. Permite ingresar una URL larga y obtener una versión corta que redirige a la original.
Las urls se almacenaran en un json llamado urls.json.

## 🚀 Despliegue en local

Para desplegar este proyecto en **local**, sigue los siguientes pasos.

1. **Clonar el repositorio**:
   Si aún no tienes el repositorio en tu máquina local, clónalo:
   ```bash
   git clone https://github.com/tu-usuario/link-shortener.git
   cd link-shortener

2. **Crear un entorno virtual**:
   Crea un entorno virtual para manejar las dependencias del proyecto. Si no tienes virtualenv instalado, puedes hacerlo con:
   ```bash
   pip install virtualenv
   python -m venv venv
   .\venv\Scripts\activate

3. **Instalar las dependencias**:
   Con el entorno virtual activado, instala las dependencias del proyecto:
   ```bash
   pip install -r requirements.txt

4. **Ejecutar la aplicacion**:
   La aplicación se ejecutará en http://127.0.0.1:5000/ por defecto. Abre esta URL en tu navegador:
   ```bash
   python app.py