def number_in_range(val_input, gt, ge, lt, le):
    """
    Function to determine if an input value is within the optional range
    :param val_input: value to be checked
    :param gt: optional greater than parameter
    :param ge: optional greater than or equal to parameter
    :param lt: optional less than parameter
    :param le: optional less than or equal to parameter
    :return: true or false
    """
    if gt is not None and val_input <= gt:
        print(f"Number must be greater than {gt}.")
        return False
    if ge is not None and val_input < ge:
        print(f"Number must be greater than or equal to {ge}.")
        return False
    if lt is not None and val_input >= lt:
        print(f"Number must be less than {lt}.")
        return False
    if le is not None and val_input > le:
        print(f"Number must be less than or equal to {le}.")
        return False
    return True

def input_int(prompt="\nPlease enter a whole number: ", error="\nInput must be a whole number!",
              gt=None, ge=None, lt=None, le=None):
    """
    This function asks the user to enter a whole number and validates input
    :param prompt: optional prompt to ask for input
    :param error: optional error message for invalid input
    :param gt: optional greater than parameter
    :param ge: optional greater than or equal to parameter
    :param lt: optional less than parameter
    :param le: optional less than or equal to parameter
    :return: the validated user input
    """
    while True:
        try:
            val_string = input(prompt)
            val_input = int(val_string)
            if number_in_range(val_input, ge, gt, le, lt):
                return val_input
            print(error)
        except ValueError:
            print(error)


def input_float(prompt="\nPlease enter a decimal number: ", error="\nInput must be a decimal number!",
                gt=None, ge=None, lt=None, le=None):
    """
    This function asks the user to type in a decimal number and validates the input
    :param prompt: optional prompt to ask for input
    :param error: optional error message for invalid input
    :param gt: optional greater than parameter
    :param ge: optional greater than or equal to parameter
    :param lt: optional less than parameter
    :param le: optional less than or equal to parameter
    :return: the validated user input
    """
    while True:
        try:
            val_string = input(prompt)
            val_input = float(val_string)
            if number_in_range(val_input, ge, gt, le, lt):
                return val_input
            print(error)
        except ValueError:
            print(error)


def input_string(prompt="\nPlease enter a piece of text: ", error="\nInput must be a piece of text!",
                 valid=lambda x: len(x) > 0):
    """
    This function asks the user to type in a piece of text and validates the input
    :param prompt: optional prompt to ask for input
    :param error: optional error for invalid input
    :param valid: optional argument which is a validation function for input
    :return: the validated user input
    """
    while True:
        try:
            val_input = input(prompt)
            if valid(val_input):
                return val_input
            print(error)
        except ValueError:
            print(error)


def y_or_n(prompt="\nPlease enter either 'y' or 'n': ", error="\nInvalid input!"):
    """
    This function asks the user to answer a yes or no question and validates the input
    :param prompt: optional yes or no question to ask for user input
    :param error: optional error for invalid input
    :return: True for yes or False for no
    """
    while True:
        val_input = input(prompt).lower()
        if val_input in ['yes', 'y']:
            return True
        if val_input in ['no', 'n']:
            return False
        else:
            print(error)


def select_item(prompt="\nPlease select an option: ", error="\nInvalid option", options=None, mapping=None):
    """
    This function takes a list of choices, prompts the user to select a choice, and validates the input
    :param prompt: optional prompt to ask for input
    :param error: optional error for invalid input
    :param options: list of choices
    :param mapping: optional dictionary that maps possible inputs to specific options
    :return: the choice selected by the user
    """
    if options is None:
        error = "No options to choose from"
        return error
    value_dict = {}
    for option in options:
        value_dict[option.lower()] = option
    if mapping is not None:
        for key in mapping:
            value_dict[key.lower()] = mapping[key]
    while True:
        print(prompt)
        val_input = input("Enter your choice: ").lower()
        if val_input in value_dict:
            return value_dict[val_input]
        print(error)

def select_item_from_list(prompt="\nPlease select an option: ", error="\nInvalid option", options=None, mapping=None):
    """
    This function takes a list of choices, prints the list, prompts the user to select a choice, and validates the input
    :param prompt: optional prompt to ask for input
    :param error: optional error for invalid input
    :param options: list of choices
    :param mapping: optional dictionary that maps possible inputs to specific options
    :return: the choice selected by the user
    """
    if options is None:
        error = "No options to choose from"
        return error
    value_dict = {}
    for option in options:
        value_dict[option.lower()] = option
    if mapping is not None:
        for key in mapping:
            value_dict[key.lower()] = mapping[key]
    while True:
        print(prompt)
        for index, choice in enumerate(options, start=1):
            print(f"{index}. {choice}")
        val_input = input("Enter your choice: ").lower()
        if val_input.isdigit():
            index = int(val_input)
            if 1 <= index <= len(options):
                return options[index - 1]
        if val_input in value_dict:
            return value_dict[val_input]
        print(error)

def input_value(type_input, *args, **kwargs):
    """
    This function takes a type keyword arguments and executes the appropriate function
    :param type_input: type keyword argument
    :param kwargs: optional arguments to pass to the function, prompt
    :return: user input from executed function
    """
    if type_input == 'int':
        val_input = input_int(*args, **kwargs)
        return val_input
    elif type_input == 'float':
        val_input = input_float(*args, **kwargs)
        return val_input
    elif type_input == 'str':
        val_input = input_string(*args, **kwargs)
        return val_input
    elif type_input == 'y_or_n':
        val_input = y_or_n(*args, **kwargs)
        return val_input
    elif type_input == 'select':
        val_input = select_item(*args, **kwargs)
        return val_input
    else:
        print('Invalid Type')

'''
def number_in_range(value, ge, gt, le, lt):
    if ge is not None and value < ge:
        return False
    if gt is not None and value <= gt:
        return False
    if le is not None and value > le:
        return False
    if lt is not None and value >= lt:
        return False


def input_int(prompt = "Please enter a whole number: ", error = "Input must be a whole number!",
              ge=None, gt=None, lt=None, le=None):
    while True:
        try:
            val_string = input(prompt)
            val_int = int(val_string)
            if number_in_range(val_int, ge, gt, le, lt):
                return val_int
            print(f"Value must be in range")
        except ValueError:
            print(error)

def yes_or_no(prompt = "Please enter yes or no", error = "Input must be yes or no"):
    while True:
        val = input(prompt).lower()
        if val in ["yes", "y"]:
            return True
        if val in ["no", "n"]:
            return False
'''