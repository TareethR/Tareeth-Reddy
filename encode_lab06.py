def encode_password(password):
    encoded_password = ""
    for digit in password:
        shifted_digit = str((int(digit) + 3) % 10)
        encoded_password += shifted_digit
    return encoded_password


def decode_password(encoded_password):
    flassword = [int(x) for a, x in enumerate(str(encoded_password))]
    pass_word = [x - 3 if x > 3 else x + 7 for x in flassword]
    decoded_password = ""
    for y in pass_word:
        decoded_password += str(y)
        int(decoded_password)
    return decoded_password


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
    if decision == "2":
        decoded_password = decode_password(encoded_password)
        print("The encoded password is", encoded_password, "and the original password is", decoded_password)




    elif decision == "3":
        break
    else:
        print("Invalid option. Please try again.")