https://flask.palletsprojects.com/es/main/quickstart/

INICIAR PROYECTO

Creamos un entorno virtual en la carpeta del proyecto
~$ python -m venv venv

Activamos los scripts WINDOWS → .\venv\Scripts\activate  
macOS/Linux → source venv/bin/activate

INSTALAR PAQUETES (requirements.txt)

~$ pip install -r requirements.txt

¿Opcional?
https://googlechromelabs.github.io/chrome-for-testing/#stable

INICIAMOS PROYECTO

~$ flask --app app run

~$ flask run

~$ flask --app app --debug run 

De esta forma, si ejecutamos app.py no tendremos que estar cerrando y abriendo el proyecto para ver los cambios que hagamos. Bastará con recargar la página.

¿OPCIONAL? → Nos ponemos en modo “development”

En Windows → ~$ set FLASK_ENV=development

ACCEDEMOS A L APLICACIÓN EN EL NAVEGADOR:

http://127.0.0.1:5000/
