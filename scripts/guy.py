import os

class Guy:
    guys = dict()

    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
        Guy.guys[self.name] = self

    def __repr__(self) -> str:
        return f"It's {self.name}. He is {self.age}. And he works as {self.job}"

    def show_data(self):
        return f"It's {self.name}. He is {self.age}. And he works as {self.job}"


if __name__ == "__main__":
    sergay = Guy("sergay", 20, "it")
    sergay = Guy("nikita", 20, "it")
    matvey = Guy("matvey", 20, "gay")

    while 1:
        name = input("Enter name: ")
        print(Guy.guys[name].show_data())

        if input("yes? ") == "yes":
            name = input("name")

            # "os.system("reboot") # will work and reboot computer
            eval(name + ".show_data")