class InvalidChoice(Exception):
    def __init__(self, message = 'Please choose an available square'):
        self.message = message
        super().__init__(self.message)