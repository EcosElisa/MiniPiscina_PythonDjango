class Intern:
    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.Name = name

    def __str__(self):
        return self.Name

    def make_coffee(self):
        return Coffee()

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")


class Coffee:
    def __str__(self):
        return "This is the worst coffee you ever tasted."


# Testes
if __name__ == "__main__":
    # Instanciando o primeiro intern sem nome
    print("---------------------------------------------------------------------------")
    intern1 = Intern()
    print("                       First intern                                        ")
    print(intern1);
    # Pedindo ao outro intern para trabalhar
    try:
        intern1.work()
    except Exception as e:
        print(e)

    # Instanciando o segundo intern com o nome "Mark"
    print("---------------------------------------------------------------------------")
    intern2 = Intern("Mark")
    print("                       Second intern                                        ")
    print(intern2)
    # Pedindo a Mark para fazer café
    coffee = intern2.make_coffee()
    print(coffee)

   
