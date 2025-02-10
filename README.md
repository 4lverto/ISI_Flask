# SuperCompare

SuperCompare es una herramienta para comparar los precios de los productos en supermercados latinoamericanos como PlazaVea, Jumbo, y SantaIsabel.
Para el desarrollo de este proyecto he trabajado con incorporación de API's y la técnica de Web Scrapping para extraer determinados elementos de páginas web.

## Descripción

SuperCompare permite a los usuarios buscar productos específicos y comparar sus precios en diferentes supermercados. La aplicación utiliza Selenium para realizar scraping de los datos de los supermercados y Flask para servir la aplicación web.

## Requisitos

- Python 3.x
- pip (gestor de paquetes de Python)
- Git
- ChromeDriver (para Selenium)

## Instalación

### 1. Clonar el repositorio

Primero, clona este repositorio en tu máquina local:

git clone https://github.com/4lverto/supercompare.git
cd supercompare

### 2. Crear y activar un entorno virtual

Crea un entorno virtual para el proyecto y actívalo:

python -m venv venv
source venv/bin/activate  # En Unix/macOS
venv\Scripts\activate     # En Windows

### 3. Instalar las dependencias

Instala las dependencias necesarias usando pip:

pip install -r requirements.txt

### 4. Configurar las variables de entorno

Crea un archivo .env en el directorio raíz del proyecto con el siguiente contenido:

FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=mysecretkey
FLASK_CONFIG=development

### 5. Descargar y configurar ChromeDriver
 ## Descargar ChromeDriver

1. Ve a la página de descargas de ChromeDriver.
2. Descarga la versión de ChromeDriver que coincide con tu versión de Chrome.
3. Descomprime el archivo descargado.

 ## Configurar ChromeDriver

   # En Windows:
    
1. Mueve chromedriver.exe a una ubicación conveniente, por ejemplo, C:\chromedriver.
2. Añade C:\chromedriver a tu variable de entorno PATH:
    * Abre el Panel de Control y busca "Variables de entorno".
    * En las Variables del sistema, selecciona la variable Path y haz clic en "Editar".
    * Añade C:\chromedriver.

    # En Unix/macOS
1. Mueve chromedriver a /usr/local/bin:
sudo mv chromedriver /usr/local/bin/

2. Asegúrate de que el archivo tenga permisos de ejecución:
sudo chmod +x /usr/local/bin/chromedriver

### 6. Ejecutar la aplicación

Finalmente, ejecuta la aplicación Flask:
flask run


### USO:
1. Abre tu navegador web y navega a http://127.0.0.1:5000.
2. Introduce el nombre de un producto en la barra de búsqueda y haz clic en "Buscar".
3. La aplicación mostrará los precios del producto en diferentes supermercados y destacará el más barato.

### CONTRIBUCIÓN
Si deseas contribuir a este proyecto:

1. Haz un fork del proyecto.
2. Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
3. Realiza los cambios necesarios y haz commit (git commit -am 'Agrega nueva funcionalidad').
4. Sube los cambios a tu repositorio (git push origin feature/nueva-funcionalidad).
5. Crea un nuevo Pull Request.
