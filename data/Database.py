from logic.Site import Site
from logic.RegisteredSite import RegisteredSite

class Database:
    @staticmethod
    def read_bookmarks():
        return [
            Site("https://www.google.com/", "Google Search", "Biggest search engine"),
            RegisteredSite("https://www.pcc.edu/", "PCC Homepage", "My school",
                           "kristen.gally", "xxx"),
            Site("http://www.imdb.com/", "IMDB Search", "Entertainment"),
            RegisteredSite("https://www.yahoo.edu/", "yahoo", "yahoo",
                           "kristen.gally", "xxx"),
            Site("http://www.abc.com/", "defg", "hijk")
        ]