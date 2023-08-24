class NullError(Exception):
    def __init__(self, *message):
        if message:
            self.message = message[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"NullError: {self.message}"
        return 'NullError'
