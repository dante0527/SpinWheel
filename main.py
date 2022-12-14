import os
from random import choice
from time import sleep

options = [
    "Kaisen",
    "Package Storeeeeeeee",
    "Hangar",
    #"Chinese",
    #"Stop & Shop",
    #"Spin Again",
    #"Chipotle",
    #"Classic Burger",
    #"Shake Shack",
    #"Docon Meatballs",
    #"Dan's Choice"
]

# Clear screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# Display list of options
def showOptions(title: str = "Remaining Options:"):
    print(f"\n{title}\n")
    for option in options:
        print(option)
    print()

# Print random choice from options with decreasing speed
def spin(mode: str = "elim"):

    # Start Message
    clear()
    showOptions("Options:")
    input("Spin the wheel...")

    while len(options) > 1:

        # Set width of wheel
        width = 0
        for option in options:
            if len(option) > width:
                width = len(option) + 4

        # First 5 choices
        c1 = choice(options)
        c2 = choice(options)
        c3 = choice(options)
        c4 = choice(options)
        c5 = choice(options)

        # Spin Wheel
        for i in range(125):
            clear()

            # Roll choices
            if i < 124:
                c1 = c2
                c2 = c3
                c3 = c4
                c4 = c5
                c5 = choice(options)

            # Print random choice
            print(
                "Spinning Wheel!\n" if i < 124 else f"{options.pop(options.index(c3))} has been eliminated!\n",
                ' ', '_' * (width), '\n',
                '|', (' ' * width), '|\n',
                '|', c1.center(width), '|\n',
                '|', c2.center(width), '|\n',
                '|->', c3.center(width-4), '<-|\n',
                '|', c4.center(width), '|\n',
                '|', c5.center(width), '|\n',
                '|', '_' * (width), '|'
                )

            # Display Remaining Options
            if len(options) > 1:
                showOptions()

            # Decrease speed of wheel as it spins
            match i:
                case _ if i < 100:
                    sleep(i * 0.001)
                case _ if i < 115:
                    sleep(0.3)
                case _ if i < 121:
                    sleep(0.5)
                case _ if i < 124:
                    sleep(1)
                case _:
                    input("\nSpin again..." if len(options) > 1 else f"\nWinner is {options[0]}!!!")


if __name__ == "__main__":
    spin()
