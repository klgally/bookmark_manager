from logic.Site import Site

class ConsoleUI:
    bookmarks = None

    @staticmethod
    def print_menu():
        print("Options for the bookmark manager: ")
        print("Exit")


    @classmethod
    def init(cls):
        cls.bookmarks = Site.read_bookmarks()


    @classmethod
    def run(cls):
        while True:
            cls.print_menu()
            choice = select_item("Please select an option: ", choices=["x"])


if __name__ == "__main__":
    ConsoleUI.init()
    ConsoleUI.run()