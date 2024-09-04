class MaxAmount_err(Exception):
    def __init__(self, message, name, first_name):
        super().__init__()
        self.message = message
        self.name = name
        self.first_name = first_name

    def get_exception_message(self):
        return self.message

