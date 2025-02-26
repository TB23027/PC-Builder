pc_parts = []
print("Options:")
print("1. Add a component")
print("2. Remove a component")
print("3. View Build")
print("4. Finish and exit")
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

        elif option == 3:
            print(pc_parts)

        elif option == 4:
            break

    except ValueError:
        print("Enter a proper integer: ")

print(f"Final Computer Build {pc_parts}")
print("Goodbye")