class AppError(Exception):
    code = 'ERR101'
    template = 'Encounted to unspecified error'

    def __init__(self, *args):
        super().__init__(*args)

    def info(self):
        return {
            'code': self.code
        }

class ParserError(AppError):
    def __init__(self):
        super().__init__("Have no any condition support for this parser")