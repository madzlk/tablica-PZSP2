def print_hello():
    """
    Print out hello message to the console.
    """
    print("Hello world")

def say_hi(name):
    """
    Return a welcoming statement.

    :param name: required name of welocmed person.
    :type name: str.
    :return: message with welocome statement.
    :rtype: str.

    """
    return f'Hi {name}'

def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]

    """
    return ["eggs", "bacon", "spam"]