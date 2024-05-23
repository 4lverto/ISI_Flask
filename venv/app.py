from flask import Flask, render_template, request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    items = []
    query = ''  # Inicializar query para evitar UnboundLocalError
    if request.method == 'POST':
        query = request.form['query']
        search_url = f'https://www.plazavea.com.pe/search/?_query={query}'
        app.logger.debug(f"URL de búsqueda: {search_url}")

        # Configuración de Selenium
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Ejecuta Chrome en modo headless (sin interfaz gráfica)
        driver = webdriver.Chrome(options=chrome_options)
        
        try:
            driver.get(search_url)
            time.sleep(5)  # Espera 5 segundos para que la página se cargue completamente
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            # Buscar todos los contenedores de productos
            found_details = soup.find_all('div', class_='Showcase__content')
            app.logger.debug(f"Productos encontrados: {len(found_details)}")

            # Limitar a los primeros 6 productos
            for details in found_details[:6]:
                app.logger.debug(f"Detalles del producto HTML: {details.prettify()}")
                name_tag = details.find('a', class_='Showcase__name')
                if name_tag:
                    title = name_tag.get_text(strip=True)  # Obtener el texto del enlace
                    app.logger.debug(f"Producto: {title}")
                    price_tag = details.find('div', class_='Showcase__salePrice')
                    if price_tag:
                        app.logger.debug(f"Encontrado price_tag: {price_tag}")
                        if 'data-price' in price_tag.attrs:
                            price = price_tag['data-price']
                            app.logger.debug(f"Precio: {price}")  # Mensaje de depuración para ver el precio del producto
                        else:
                            price = "Precio no disponible"
                            app.logger.debug(f"data-price no encontrado en price_tag para el producto {title}")
                    else:
                        price = "Precio no disponible"
                        app.logger.debug(f"price_tag no encontrado para el producto {title}")
                    items.append({'title': title, 'price': price})
                else:
                    app.logger.debug("Nombre del producto no encontrado")
        except Exception as e:
            app.logger.error(f"Error al procesar la solicitud: {e}")
        finally:
            driver.quit()

    return render_template('index.html', items=items, query=query)

if __name__ == '__main__':
    app.run(debug=True)
