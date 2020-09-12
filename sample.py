from recipe_scrapers import scrape_me

# give the url as a string, it can be url from any site listed below
scraper = scrape_me('https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/')

print("\n- Title - ")
print(scraper.title())
# scraper.total_time()
# scraper.yields()
print("\n- Ingredients -")
for x in scraper.ingredients():
    print(x)
# scraper.instructions()
# scraper.image()
# scraper.links()