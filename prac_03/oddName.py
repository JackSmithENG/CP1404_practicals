""" Jack Smith
name = input("Enter name:")
while name =="":
    print("Invalid name")
    name = input("Enter name:")

print(name[::2]) """

def main():
    name = get_name()
    print_parts(name, 3)


def print_parts(name, step=2):
    print(name[::step])


def get_name():
    name = input("Name: ")
    while name == "":
        print("Invalid name.")
        name = input("Name: ")
    return name


main()