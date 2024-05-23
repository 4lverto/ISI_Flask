from flask import Flask, render_template, request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    print("Entrando en la función index")
    items = []
    query = ''  # Inicializar query para evitar UnboundLocalError
    if request.method == 'POST':
        print("Método POST detectado")
        query = request.form['query']
        print(f'Consulta recibida: {query}')
        search_url = f'https://www.plazavea.com.pe/search/?_query={query}'
        print(f'URL de búsqueda: {search_url}')

        # Configuración de Selenium
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Ejecuta Chrome en modo headless (sin interfaz gráfica)
        driver = webdriver.Chrome(options=chrome_options)
        
        try:
            driver.get(search_url)
            time.sleep(5)  # Espera 5 segundos para que la página se cargue completamente
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            print("HTML parseado correctamente")

            # Imprimir una parte del HTML para verificar la estructura
            print("HTML de respuesta (primeros 2000 caracteres):")
            print(soup.prettify()[:2000])

            # Buscar todos los enlaces con la clase 'Showcase__name'
            found_details = soup.find_all('a', class_='Showcase__name')
            print(f"Número de elementos encontrados con la clase 'Showcase__name': {len(found_details)}")

            for i, details in enumerate(found_details):
                print(f"Elemento {i}: {details.prettify()}")
                title = details.get_text(strip=True)  # Obtener el texto del enlace
                print(f"Producto encontrado: {title}")
                items.append({'title': title})

        finally:
            driver.quit()

    else:
        print("Método GET detectado")

    return render_template('index.html', items=items, query=query)

if __name__ == '__main__':
    app.run(debug=True)
