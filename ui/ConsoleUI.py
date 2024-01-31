from logic.Site import Site
from ui.input_validation import *
from logic.Category import Category

class ConsoleUI:
    __all_bookmarks = None
    __all_categories = None

    CHOICES = ["p", "c", "s", "a", "d", "x"]

    @staticmethod
    def print_menu():
        print()
        print("Options for the bookmark manager: ")
        print("    p: Print the bookmarks")
        print("    c: Print the categories")
        print("    s: Print bookmarks for selected category")
        print("    a: Add a new category")
        print("    d: Delete an existing category")
        print("    x: Exit the program")

    @classmethod
    def init(cls):
        cls.__all_bookmarks, cls.__all_categories = Category.read_data()

    @classmethod
    def print_bookmarks(cls):
        for bookmark in cls.__all_bookmarks:
            print(bookmark)

    @classmethod
    def print_categories(cls):
        for category in cls.__all_categories:
            print(category.get_name())

    @classmethod
    def select_category(cls):
        names = [category.get_name() for category in cls.__all_categories] +["exit"]
        selected = select_item_from_list(prompt="Please select a Category: ", options=names)
        if selected == "exit":
            return None
        print("Selected: ", selected)
        selected_category = Category.lookup(selected)
        return selected_category

    @classmethod
    def print_selected_category(cls):
        selected = cls.select_category()
        if selected is None:
            return
        print(f"Bookmarks for {selected.get_name()}: ")
        for bookmark in selected:
            print("    ", bookmark)

    @classmethod
    def new_category(cls):
        while True:
            name = input_string("Please enter a new Category name: ")
            try:
                category = Category.lookup(name)
                if category is not None:
                    print(f"Error! Category {name} already exists!")
                    continue
            except KeyError:
                pass
            if name.lower() == 'exit':
                return
            description = input_string("Please enter a description for the category: ")
            category = Category(name, description, [])
            cls.__all_categories.append(category)
            print(f"New Category {name} was added")
            return

    @classmethod
    def delete_category(cls):
        selected = cls.select_category()
        if selected is None:
            return
        if selected.get_name() == Category.ALL_BOOKMARKS:
            print(f"Error! Cannot delete the {Category.ALL_BOOKMARKS} category.")
            return
        if selected not in cls.__all_categories:
            print(f"Error! Category {selected.get_name()} does not exist")
            return
        cls.__all_categories.remove(selected)


    @classmethod
    def run(cls):
        while True:
            cls.print_menu()
            choice = select_item("Please select an option for the Bookmark Manager: ",
                                 "Please select one of the above items", options=cls.CHOICES)
            if choice == "x":
                print("Goodbye")
                break
            elif choice == "p":
                cls.print_bookmarks()
            elif choice == "c":
                cls.print_categories()
            elif choice == "s":
                cls.print_selected_category()
            elif choice == "a":
                cls.new_category()
            elif choice == "d":
                cls.delete_category()



if __name__ == "__main__":
    ConsoleUI.init()
    ConsoleUI.run()
