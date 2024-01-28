class Database:
    @staticmethod
    def read_bookmarks():
        return [
            Site("https://www.google.com/", "Google Search", "Biggest search engine"),
            RegisteredSite("https://www.pcc.edu/", "PCC Homepage", "My school", "kristen.gally", "xxx"),
            Site("http://www.imdb.com/", "IMDB Search", "Entertainment")
        ]