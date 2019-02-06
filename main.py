from Task import Color


def prn():
    user_text = input("Enter some text: ")
    try:
        user_input = int(input("""Enter text color:\n 1: RED\n 2: GREEN\n 3: YELLOW\n Your choise: """))
        back = int(input("""Enter background color:\n 11: CYAN\n 10: WHITE\n  Your choise: """))
    except ValueError as ex:
        print("This is not number, try again. ", ex)
        return

    color = Color.int_to_color(user_input)
    back = Color.int_to_color(back)

    with Color(color, back):
        print(user_text)


if __name__ == '__main__':
    prn()
