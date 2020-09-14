import webbrowser
from recipe_scrapers import scrape_me

# give the url as a string, it can be url from any site listed below
scraper = scrape_me('https://thewoksoflife.com/cumin-lamb-biang-biang-noodles/')
# scraper = scrape_me('https://thewoksoflife.com/cantonese-steamed-fish/')


# print("\n- Title - ")
# print(scraper.title())
# # scraper.total_time()
# # scraper.yields()
# print("\n- Ingredients -")
# for x in scraper.ingredients():
#     print(x)
# print("\n- Instructions -")
# print(scraper.instructions())
# # webbrowser.open(scraper.image())
# # scraper.links()


print(
    scraper.title() + "\n" +
    # scraper.total_time() + "\n"
    # scraper.yields() + "\n"
    # scraper.ingredients() + "\n"
    scraper.instructions() + "\n" +
    scraper.image() + "\n"
    # scraper.links()
)

