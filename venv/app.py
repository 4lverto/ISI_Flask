from flask import Flask, render_template, request
from scraper_plazavea import scrape_plazavea
#from scraper_hipercor import scrape_hipercor
#from scraper_carrefour import scrape_carrefour

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    items = []
    query = ''
    if request.method == 'POST':
        query = request.form['query']
        items_plazavea = scrape_plazavea(query)
        #items_hipercor = scrape_hipercor(query)
        #items_carrefour = scrape_carrefour(query)
        items = {
            'PlazaVea': items_plazavea#,
            #'Hipercor': items_hipercor,
            #'Carrefour': items_carrafour

        }
    return render_template('index.html', items=items, query=query)

if __name__ == '__main__':
    app.run(debug=True)
