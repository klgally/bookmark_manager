class Site:
    url = ""
    title = ""
    description = ""
    icon = None

    @staticmethod
    def read_bookmarks():
        from data.Database import Database

        return Database.read_bookmarks()
