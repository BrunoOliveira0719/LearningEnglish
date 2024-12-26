class HttpNotFound(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message
        self.name = "NotFound"
        self.status_code = 404