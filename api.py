import flask
from flask import request, jsonify
import webbrowser
from recipe_scrapers import scrape_me

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Cocina Recipe Scraper</h1><p>A prototype API for getting structured recipe data from food blogs.</p>'''

@app.route('/api/v1/resources/recipes', methods=['GET'])
def api_url():
    # Check if an url was provided as part of the URL.
    # If url is provided, assign it to a variable.
    # If no url is provided, display an error in the browser.
    if 'recipe_url' in request.args:
        recipe_url = request.args['recipe_url']
    else:
        return "Error: No recipe_url field provided. Please specify a recipe_url."

    # Create scraper object
    scraper = scrape_me(recipe_url)

    # Use the jsonify function from Flask to convert our recipe 
    # attributes to the JSON format.
    return jsonify(
        title=scraper.title(),
        photo=scraper.image(),
        yields=scraper.yields(),
        ingredients=scraper.ingredients(),
        instructions=scraper.instructions(),
    )
    return jsonify(results)

app.run()
