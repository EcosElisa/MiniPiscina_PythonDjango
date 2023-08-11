def my_var():
    itens = [42, '42', 'quarante-deux', 42.0, True, [42], {42: 42}, (42,), set()]

    for item in itens:
        print(item, 'has a type ', type(item))

if __name__ == '__main__':
    my_var()

