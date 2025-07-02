enter_input = input('''Enter the name or "ex" to exit: ''')

# while (enter_input != "ex"):
#     enter_input = input('''Enter the name or "ex" to exit: ''')
#     print(enter_input)
# print("loops Ends")
# print("Exited the loop")


# The code will keep asking for input until the user types "ex"

while True:
    enter_input = input('''Enter the name or "ex" to exit: ''')
    if enter_input.lower() == "ex":
        print("Exited the loop")
        break
    else:
        print(f"You entered: {enter_input}")