class Color:
    RED = '033'

    def __init__(self, color):
        self.color = color 

    def __enter__(self):
        print('\033[{}m''\033[31m'.format(self.color))

    def __exit__(self, exc_type, exc_value, tb):
        print('\033[00m')
