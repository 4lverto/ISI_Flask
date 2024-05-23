from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def get_product_names(details):
    names = []
    for detail in details:
        name_tag = detail.find('a', class_='Showcase__name')
        if name_tag:
            title = name_tag.get_text(strip=True)
            names.append(title)
        else:
            names.append("Nombre no disponible")
    return names

def get_product_prices(details):
    prices = []
    for detail in details:
        price_tag = detail.find('div', class_='Showcase__salePrice')
        if price_tag and 'data-price' in price_tag.attrs:
            price = price_tag['data-price']
        else:
            price = "Precio no disponible"
        prices.append(price)
    return prices

def get_product_images(details):
    images = []
    for detail in details:
        img_tag = detail.find('figure', class_='Showcase__photo').find('img')
        if img_tag and 'src' in img_tag.attrs:
            img_url = img_tag['src']
            images.append(img_url)
        else:
            images.append("Imagen no disponible")
    return images

def scrape_plazavea(query):
    search_url = f'https://www.plazavea.com.pe/search/?_query={query}'
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        driver.get(search_url)
        time.sleep(5)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        found_details = soup.find_all('div', class_='Showcase__content')

        # Para limitar a los primeros 6 productos, descomentar la siguiente línea
        #details_to_process = found_details[:6]
        
        # También deberemos sustituir "found_details" por "details_to_process" en las 3 siguientes líneas
        
        names = get_product_names(found_details)
        prices = get_product_prices(found_details)
        images = get_product_images(found_details)

        products = []
        for name, price, image in zip(names, prices, images):
            products.append({'title': name, 'price': price, 'image': image})

        return products

    except Exception as e:
        print(f"Error al procesar la solicitud: {e}")
        return []
    finally:
        driver.quit()
