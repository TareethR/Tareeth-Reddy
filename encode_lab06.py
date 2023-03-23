def encode_password(password):
    encoded_password = ""
    for digit in password:
        shifted_digit = str((int(digit) + 3) % 10)
        encoded_password += shifted_digit
    return encoded_password

while True:
    print("Menu")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    decision = input("Please enter an option: ")

    if decision == "1":
        password = input("Please enter your password to encode: ")
        encoded_password = encode_password(password)
        print("Your password has been encoded and stored!")
    




    elif decision == "3":
        break
    else:
        print("Invalid option. Please try again.")