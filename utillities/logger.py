class Logger():
    def __init__(self, filename):
        self.filename = filename

    def debug(self, message):
        self.log('DEBUG: ' + message)

    def info(self, message):
        self.log('INFO: ' + message)

    def error(self, message):
        self.log('ERROR: ' + message)

    def log(self, message):
        print('("' + self.filename + '")' + ' ' + message)
