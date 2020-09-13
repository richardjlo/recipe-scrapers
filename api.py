import flask
from flask import request, jsonify
import webbrowser
from recipe_scrapers import scrape_me

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1><p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

@app.route('/api/v1/resources/recipes', methods=['GET'])
def api_url():
    # Check if an url was provided as part of the URL.
    # If url is provided, assign it to a variable.
    # If no url is provided, display an error in the browser.
    if 'recipe_url' in request.args:
        # recipe_url = int(request.args['recipe_url'])
        recipe_url = request.args['recipe_url']
        # print(request.args['recipe_url'])
        # recipe_url = 'https://thewoksoflife.com/cumin-lamb-biang-biang-noodles/'
    else:
        return "Error: No recipe_url field provided. Please specify a recipe_url."

    # Create scraper object
    scraper = scrape_me(recipe_url)

    # Use the jsonify function from Flask to convert our recipe 
    # attributes to the JSON format.
    return jsonify(
        title=scraper.title(),
        yields=scraper.yields(),
        instructions=scraper.instructions(),
    )
    return jsonify(results)

app.run()
