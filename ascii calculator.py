while True:
    user_input = input("enter any key to print (enter 'q' to quit): \n")
    print("user input was:", user_input)
    print("the value of", user_input, "in ASCII us:", str(ord(user_input)), "\n\n\n")

    if user_input == "q":
        print("ending program")
        break