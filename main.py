from Task import Color


def prn():
    with Color(Color.RED):
        print("Это красная строка")
        print("Это тоже красная строка")


if __name__ == '__main__':
    prn()
