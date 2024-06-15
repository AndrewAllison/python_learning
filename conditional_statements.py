"""
Simple example of conditional statements
"""


def conditional_statements():
    """
    This is some conditional types
    :return:
    """
    number_input = input("Enter a number between 1 and 100")
    number = int(number_input)

    if number > 100 or number < 0:
        print("The number is invalid")
    else:
        print("Great that was correct")


if __name__ == "__main__":
    conditional_statements()
