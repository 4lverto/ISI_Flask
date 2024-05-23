from flask import Flask, render_template, request
from scraper_plazavea import scrape_plazavea
from scraper_jumbo import scrape_jumbo

app = Flask(__name__)

def clean_price(price_str):
    price_str = price_str.replace('$', '').replace('S/', '').strip()
    try:
        return float(price_str)
    except ValueError:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    items = {'PlazaVea': [], 'Jumbo': []}
    query = ''
    cheapest_product = None

    if request.method == 'POST':
        query = request.form['query']
        
        items['PlazaVea'] = scrape_plazavea(query)
        items['Jumbo'] = scrape_jumbo(query)
        
        # Find the cheapest product
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
