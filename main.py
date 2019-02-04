from Task import Color


def prn():
    user_text = input("Enter some text: ")
    user_input = input("""Enter color:\n 1: RED\n 2: GREEN\n 3: YELLOW\n Your choise: """)
    # TODO check for int

    color = Color.str_to_color(user_input)
    
    with Color(color):
        print(user_text)


if __name__ == '__main__':
    prn()
