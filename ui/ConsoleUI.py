from logic.Site import Site
from ui.input_validation import select_item

class ConsoleUI:
    bookmarks = None

    @staticmethod
    def print_menu():
        print()
        print("Options for the bookmark manager: ")
        print("    p: Print the bookmarks")
        print("    x: Exit the program")

    @classmethod
    def init(cls):
        cls.bookmarks = Site.read_bookmarks()

    @classmethod
    def print_bookmarks(cls):
        for bookmark in cls.bookmarks:
            print(bookmark)

    @classmethod
    def run(cls):
        while True:
            cls.print_menu()
            choice = select_item("Please select an option for the Bookmark Manager: ",
                                 "Please select one of the above items", options=["p", "x"])
            if choice == "x":
                print("Goodbye")
                break
            elif choice == "p":
                cls.print_bookmarks()


if __name__ == "__main__":
    ConsoleUI.init()
    ConsoleUI.run()
