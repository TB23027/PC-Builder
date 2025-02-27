# This list has nothing inside as the user will enter what they want
# to add to this build during the while loop.
pc_parts = []
# Putting these print statements outside of the while loop means they 
# will only be asked once at the start and not every single repeat.
print("Options:")
print("1. Add a component")
print("2. Remove a component")
print("3. View Build")
print("4. Finish and exit")
# Anything added inside this list will be repeated 
# until the break option is done when the user enters the number
# 4 when prompted.
while True:
    try:
        # This will be printed out everytime the while loop repeats.
        print(f"Your current build {pc_parts}")
        option = int(input("Choose an option: "))
        # If the user enters no. 1, they will
        # be able to add a component to their custom pc build.
        if option == 1:
            component = input("Enter a component you wish to add: ")
            pc_parts.append(component)
            print(f"{component} added to build.")
        # If the user enters no. 2, they will
        # be able to remove a component from the custom pc build list.
        # They must enter the exact copy of whatever they previously
        # entered as the part otherwise they will have to redo it.
        elif option == 2:
            remcomponent = input("Enter the component you wish to remove: ")
            pc_parts.remove(remcomponent)
            print(f"{remcomponent} removed from build.")
        # If the user enters no. 3, the list will be printed.
        elif option == 3:
            print(pc_parts)
        # If the user enters no. 4, the while loop breaks and anything 
        # after the while loop will begin.
        elif option == 4:
            break
        # If the user enters a number above or below 1-4,
        # they will be prompted to enter a number between 1-4.
        else:
            print("1-4 please!")
    # If the user enters a letter not a number, 
    # or if the user doesn't copy the exact component when they want
    # to remove it.
    except ValueError:
        print("Make sure the spelling is correct or make sure it is an integer: ")
# These will be printed once the while loop has been broken
# after the user enters the no. 4.
print(f"Final Computer Build {pc_parts}")
print("Goodbye")