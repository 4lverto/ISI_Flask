from flask import Flask, render_template, request
from scraper_plazavea import scrape_plazavea
from scraper_jumbo import scrape_jumbo
from scraper_santaisabel import scrape_santaisabel

app = Flask(__name__)

def clean_price(price_str):
    if isinstance(price_str, str):
        price_str = price_str.replace('$', '').replace('S/', '').replace(',', '').strip()
        try:
            return float(price_str)
        except ValueError:
            return None
    return price_str

def convert_currency(price, rate):
    return price * rate

@app.route('/', methods=['GET', 'POST'])
def index():
    items = {'PlazaVea': [], 'Jumbo': [], 'SantaIsabel': []}
    query = ''
    cheapest_product = None
    conversion_rate = 240  # 1 sol peruano = 240 pesos chilenos

    if request.method == 'POST':
        query = request.form['query']
        
        items['PlazaVea'] = scrape_plazavea(query)
        items['Jumbo'] = scrape_jumbo(query)
        items['SantaIsabel'] = scrape_santaisabel(query)
        
        # Convertir precios de PlazaVea de soles a pesos
        for product in items['PlazaVea']:
            price_str = product.get('price')
            price = clean_price(price_str)
            if price is not None:
                product['price'] = convert_currency(price, conversion_rate)

        # Encontrar el producto más barato
        for store, products in items.items():
            for product in products:
                price_str = product.get('price')
                price = clean_price(price_str)
                if price is not None:
                    if not cheapest_product or price < cheapest_product['price']:
                        cheapest_product = {
                            'title': product['title'],
                            'price': price,
                            'image': product['image'],
                            'store': store
                        }

    return render_template('index.html', items=items, query=query, cheapest_product=cheapest_product)

if __name__ == '__main__':
    app.run(debug=True)
