from Task import Color


def u_input():
    print("here you could enter something")
    user_input = input("Enter something: ")
    with Color(user_input):
        print(user_input)
