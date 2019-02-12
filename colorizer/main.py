from Task import Color


def prn():
    user_text = input("Enter some text: ")
    try:
        user_input = int(input("""Enter text color:\n 1: BLACK\n 2: RED\n 3: GREEN\n 4: YELLOW
 5: BLUE\n 6: MAGENTA\n 7: CYAN\n 8: WHITE\n Your choise: """))
        
        back = int(input("""Enter background color:\n 10: BLACK\n 20: RED\n 30: GREEN\n 40: YELLOW\n
 50: BLUE\n 60: MAGENTA\n 70: CYAN\n 80: WHITE\n Your choise: """))
    
    except ValueError as ex:
        print("This is not number, try again. ", ex)
        return

    color = Color.int_to_color(user_input)
    back = Color.int_to_color(back)

    with Color(color, back):
        print(user_text)


if __name__ == '__main__':
    prn()
