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
# Anything added inside this list will be repeated until the break option is done
while True:
    try:
        print(f"Your current build {pc_parts}")
        option = int(input("Choose an option: "))

        if option == 1:
            component = input("Enter a component you wish to add: ")
            pc_parts.append(component)
            print(f"{component} added to build.")

        elif option == 2:
            remcomponent = input("Enter the component you wish to remove: ")
            pc_parts.remove(remcomponent)
            print(f"{remcomponent} removed from build.")

        elif option == 3:
            print(pc_parts)

        elif option == 4:
            break

    except ValueError:
        print("Make sure the spelling is correct or make sure it is an integer: ")

print(f"Final Computer Build {pc_parts}")
print("Goodbye")