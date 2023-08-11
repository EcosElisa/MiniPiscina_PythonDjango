def read_and_print_numbers():
    arq = "numbers.txt"
    with open(arq, "r") as arquivo:
        read_numbers = arquivo.read()
        read_numbers = read_numbers.replace(",", "\n")
        print(read_numbers)


if __name__ == '__main__':
    read_and_print_numbers()