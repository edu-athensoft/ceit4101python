"""
module : exception handling
creating Custom Exceptions

"""


class CustomError(Exception):
    pass


raise CustomError("An error occurred")
