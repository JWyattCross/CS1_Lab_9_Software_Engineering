
#Encoder function goes here

#Decoder function goes here


def main():
    #Written by James Cross
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")
        menu_select = int(input("Please enter an option: "))
        if menu_select == 1:
            encoded_value = encoder_function(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
            print("")
        elif menu_select == 2:
            print(f"The encoded password is {encoded_value}, and the original password is {decode_function(encoded_value)}")
            print("")
        elif menu_select == 3:
            return


if __name__ == "__main__":
    #Written by James Cross
    main()
