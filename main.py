from random import choice
from time import sleep
import os

options = [
    "Kaisen",
    "Package Store",
    "Hangar",
    "Chinese",
    "Stop & Shop",
    "Spin Again",
    "Chipotle",
    "Classic Burger",
    "Shake Shack",
    "Docon Meatballs",
    "Dan's Choice"
]

# Clear screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# Display list of options
def showOptions():
    print("Remaining Options:\n")
    for option in options:
        print(option)
    print()


# Print random choice from options with decreasing speed
def spin():
    for i in range(125):
        # Display remaining options
        showOptions()

        # Print random choice
        print("Spinning Wheel!\n", selection := choice(options))

        # Increasing intervals between choices, last 5 are slower
        sleep(i * 0.001 if i < 120 else 0.5)
        clear()

    return selection


if __name__ == "__main__":
    # Start Message
    clear()
    showOptions()
    input("Spin the wheel...")

    while len(options) > 1:

        # Spin and return result
        selection = spin()

        # Remove result from list
        options.remove(selection)

        # Spin again if 
        if len(options) > 1:
            showOptions()
            print(f"\n{selection} has been eliminated!")
            input("\nSpin Again...")

    # Winner
    else:
        print(f"Winner is {options[0]}!!!")
