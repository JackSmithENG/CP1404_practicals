out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file)

in_file = open("name.txt", "r")
name = in_file.read().strip()
print("Your name is", name, file=out_file)
in_file.close()

in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
sum_of_file = number1 + number2
print("Sum = {}".format(sum_of_file), file=out_file)
in_file.close()
out_file.close()
