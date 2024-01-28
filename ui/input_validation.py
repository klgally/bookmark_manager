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