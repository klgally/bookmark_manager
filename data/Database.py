from logic.Category import Category
from logic.Site import Site
from logic.RegisteredSite import RegisteredSite

class Database:
    @staticmethod
    def read_data():
        google = Site("https://www.google.com/", "Google Search", "Biggest search engine on the web.")
        bing = Site("https://www.bing.com/", "Bing Search", "Search engine from MicroSoft. Now with AI.")
        pcc = RegisteredSite("https://www.pcc.edu/", "PCC Homepage", "My school", "marc.goodman", "???")
        imdb = Site("https://www.IMDB.com/", "Internet Movie Database", "All movies, TV series, etc.")
        boa = RegisteredSite("https://bankofamerica.com/", "Bank of America", "My bank", "marc.goodman", "???")
        chase = Site("https://www.chase.com/", "Chase bank", "My wife's bank")
        hurawatch = Site("https://hurawatch.ru/", "Hurawatch", "Russia-located media pirate site")
        youtube = RegisteredSite("https://youtube.com/", "YouTube", "Video sharing site.", "Marc", "???")

        search = Category("Search Engines", "Places where you can find links.", [google, bing])
        school = Category("School", "Sites related to school.", [pcc])
        finance = Category("Finance", "Finance sites.", [boa, chase])
        entertainment = Category("Entertainment", "Entertainment Sites", [imdb, hurawatch])
        video_streaming = Category("Video Streaming", "Video streaming sites.", [hurawatch, youtube])
        all_bookmarks = Category(Category.ALL_BOOKMARKS, "All the bookmarks known to the system. Automatically updated.", [google, bing, pcc, boa, chase, hurawatch, imdb, youtube])
        all_categories = [search, school, finance, entertainment, video_streaming, all_bookmarks]

        return all_bookmarks, all_categories
