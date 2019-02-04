

class Color:
    def __init__(self, u_inp):
        self.u_inp = u_inp

    def __enter__(self):

        self.u_inp = ('\033[47m''\033[31m'"{}".format(self.u_inp))
        return self
    
    def __exit__(self, exc_type, exc_value, tb):
        if self.u_inp:
            self.u_inp = ("{}"'\033[00m''\033[00m'.format(self.u_inp))
            return self
