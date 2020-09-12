import webbrowser
from recipe_scrapers import scrape_me

# give the url as a string, it can be url from any site listed below
scraper = scrape_me('https://thewoksoflife.com/cumin-lamb-biang-biang-noodles/')

print("\n- Title - ")
print(scraper.title())
# scraper.total_time()
# scraper.yields()
print("\n- Ingredients -")
for x in scraper.ingredients():
    print(x)
# scraper.instructions()
webbrowser.open(scraper.image())
# scraper.links()